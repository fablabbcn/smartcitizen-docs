import os
import re
import yaml
from jinja2 import Environment, FileSystemLoader

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
