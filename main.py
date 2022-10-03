import os
import re
import yaml
from jinja2 import Environment, FileSystemLoader

from git import Repo
import uuid
import re
import shutil
from requests import get

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    @env.macro
    def include_tags(filename, tag = 'all'):
        """
        Include a file, optionally indicating start_line and end_line
        (start counting from 0)
        The path is relative to the top directory of the documentation
        project.
        """

        full_filename = os.path.join(env.project_dir, filename)
        with open(full_filename, 'r') as file:
            lines = file.readlines()

        klines = dict()
        pattern_tag = re.compile("(?<=>)(.*)(?=<)")

        for line in lines[4:]:

            if line.startswith('# ') or line.startswith('---'): continue
            if line.startswith('## '):

                ctag = ''.join(pattern_tag.findall(line))
                klines[ctag] = dict()
                continue

            if '*' not in line: continue
            if 'index' in line: continue

            desc = line[line.index("[")+1:line.index("]")]
            link = line[line.index("(")+1:line.index(")")]

            frontmatter = get_frontmatter(link)

            description = None
            if 'description' in frontmatter:
                description = frontmatter['description']

            level = None
            more = list()
            if 'tags' in frontmatter:
                for item in frontmatter['tags']:
                    if 'level' in item:
                        level = item.replace('level', '').strip()
                    else:
                        more.append(item)

            klines[ctag][desc] = {
                'link': link.replace('.md', ''),
            }

            if description is not None:
                klines[ctag][desc]['description'] = description

            if level is not None:
                klines[ctag][desc]['level'] = level

            if more is not None:
                klines[ctag][desc]['more'] = more

        if tag != 'all': klines = klines[tag]

        return klines

    @env.macro
    def get_file(filename):
        full_filename = os.path.join(env.project_dir, 'docs', filename)

        if os.path.exists(full_filename):
            with open(full_filename, 'r') as f:
                lines = f.readlines()
        else:
            lines = ''

        return lines

    @env.macro
    def get_frontmatter(filename):

        lines = get_file(filename)

        if '---\n' in lines:
            frontmatter = yaml.load('\n'.join(lines[1:lines[1:].index('---\n')+1]),
                Loader=yaml.SafeLoader)

        else:

            frontmatter = ''

        return frontmatter

    @env.macro
    def get_content(filename):

        lines = get_file(filename)

        if '---\n' in lines:

            content = '\n'.join(lines[lines[1:].index('---\n')+1:])

        else:

            content = lines

        return content

    @env.macro
    def get_cards(template = 'tags.html', tags = 'all', full = False):

        file_loader = FileSystemLoader('templates')

        jenv = Environment(loader=file_loader)
        template = jenv.get_template(template)

        return template.render(tags=include_tags('aux/tags.md', tags), full=full)

    @env.macro
    # Inspired by function in mkdocs-snippets-plugin
    def get_snippet_git(git_url, file_path, section_name):
        repos = dict()

        p = re.compile("^#+ ")
        m = p.search(section_name)
        if m:
            section_level = m.span()[1] - 1

            root = ""
            if repos.get(git_url) is None:
                root = "/tmp/" + uuid.uuid4().hex
                repos[git_url] = root
                Repo.clone_from(git_url, root)
            else:
                root = repos[git_url]

            content = ""

            with open(root + '/' + file_path, 'r') as myfile:
                content = myfile.read()

            p = re.compile("^" + section_name + "$", re.MULTILINE)
            start = p.search(content)
            start_index = start.span()[1]

            p = re.compile("^#{1," + str(section_level) + "} ", re.MULTILINE)

            result = ""
            end = p.search(content[start_index:])
            if end:
                end_index = end.span()[0]
                result = content[start_index:end_index + start_index]
            else:
                result = content[start_index:]

            # If there are any images, find them, copy them
            result = copy_markdown_images(root, result, only_url=False)
            return result
        else:
            return "Markdown section doesn't exist in source"

    @env.macro
    # Inspired by function in mkdocs-snippets-plugin
    def get_snippet_url(url, section_name):
        repos = dict()

        p = re.compile("^#+ ")
        m = p.search(section_name)
        if m:
            section_level = m.span()[1] - 1

            content = get(url).text

            p = re.compile("^" + section_name + "$", re.MULTILINE)
            start = p.search(content)

            if start is not None:
                start_index = start.span()[1]

                p = re.compile("^#{1," + str(section_level) + "} ", re.MULTILINE)

                result = ""
                end = p.search(content[start_index:])
                if end:
                    end_index = end.span()[0]
                    result = content[start_index:end_index + start_index]
                else:
                    result = content[start_index:]

                # If there are any images, find them, copy them
                result = copy_markdown_images(None, result, only_url=True)
            else:
                result = None
            return result
        else:
            return "Markdown section doesn't exist in source"

    @env.macro
    # Inspired by function in mkdocs-snippets-plugin
    def get_snippet_rel(file_path, section_name = None):

        with open(env.project_dir + '/' + file_path, 'r') as myfile:
            content = myfile.read()

        if section_name is None:
            extract = content.split('\n')[1:]
            return '\n'.join(extract)

        p = re.compile("^#+ ")
        m = p.search(section_name)

        if m:
            section_level = m.span()[1] - 1

            p = re.compile("^" + section_name + "$", re.MULTILINE)
            start = p.search(content)

            if start is not None:
                start_index = start.span()[1]

                p = re.compile("^#{1," + str(section_level) + "} ", re.MULTILINE)

                result = ""
                end = p.search(content[start_index:])
                if end:
                    end_index = end.span()[0]
                    result = content[start_index:end_index + start_index]
                else:
                    result = content[start_index:]
                    # Images should be in absolute paths
            else:
                result = None
            return result
        else:
            return "Markdown section doesn't exist in source"

    @env.macro
    def copy_markdown_images(tmpRoot, markdown, only_url):
        # root = os.path.dirname(os.path.dirname(self.page.url))
        # root = self.page.url
        paths = []

        p = re.compile("!\[.*\]\((.*)\)")
        it = p.finditer(markdown)
        for match in it:
            print (match)

            # Check if it's an URL
            regex = re.compile(
                    r'^(?:http|ftp)s?://' # http:// or https://
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                    r'localhost|' #localhost...
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                    r'(?::\d+)?' # optional port
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

            is_url = re.match(regex, match.group(1))
            if is_url:
                continue

            path = match.group(1)
            paths.append(path)
            if not only_url:

                # TODO - !ONLY URL CASE
                destinationPath = os.path.realpath(env.project_dir + "/" +
                                                   root + "/gen_/" + path)

                if not os.path.isfile(destinationPath):
                    print("Copying image: " + path + " to " + destinationPath)

                    os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
                    shutil.copyfile(tmpRoot + "/" + path, destinationPath)

            else:

                destinationPath = "Image can't be replaced as it's relative to markdown"

        for path in paths:
            markdown = markdown.replace(path, "gen_/" + path)

        return markdown
