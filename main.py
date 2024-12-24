import os
import re
import yaml
from jinja2 import Environment, FileSystemLoader
import fnmatch
from git import Repo
import uuid
import re
import shutil
from requests import get

DEBUG = True

def get_frontmatter(content):
    if '---\n' not in content:
        if DEBUG: print ('No frontmatter in content')
        return None

    if '---\n' in content[1:]:
        frontmatter = yaml.load('\n'.join(content[1:content[1:].index('---\n')+1]), Loader=yaml.SafeLoader)
    else:
        frontmatter = None

    return frontmatter

field_color_map = {
    'air': 'orange',
    'soil': 'red',
    'water': 'blue',
    'other': 'green'
}

colors =  ['black', 'orange', 'red', 'blue', 'green', 'gray']

def on_pre_page_macros(env):
    custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))
    environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)

    source_folder = os.path.join('docs', env.page.url)

    if source_folder != 'docs/':
        return
    if DEBUG:
        print('*****************************')
        print ('Creating cards under:')
        print (source_folder)
        print('*****************************')

    if os.path.exists(os.path.join(source_folder, '.macroignore')):
        with open(os.path.join(source_folder, '.macroignore'), 'r') as ignore_file:
            ignores = ignore_file.read().splitlines()

    for (root,_,files) in os.walk(source_folder):

        for file in files:
            if file in ignores:
                # if DEBUG: print ('\tIgnoring. Direct match')
                continue

            ignore_file = False
            for ignore in ignores:
                if (fnmatch.fnmatch(file, ignore)):
                    # if DEBUG: print (ignore)
                    ignore_file = True
                    break

            if ignore_file:
                # if DEBUG:
                    # print ('\tIgnoring. Regex match')
                    # print ('---')
                continue

            file_path = os.path.join(root, file)

            print (f'File: {file_path}')

            if os.path.exists(file_path):
                with open(file_path, 'r') as _file:
                    content = _file.readlines()

                frontmatter = get_frontmatter(content)
                if frontmatter is not None:
                    if 'card' not in frontmatter:
                        continue

                    if not frontmatter['card']:
                        if DEBUG: print ('\tNot a card!')
                        continue

                    if 'name' not in frontmatter:
                        if DEBUG: print ('\tERROR: no name in frontmatter!')
                        continue

                    frontmatter['target_url'] = '/'+file_path.replace('docs/','').replace('.md','/').replace('index/', '')

                    if 'field' in frontmatter:
                        if DEBUG: print (frontmatter['field'])

                        # We can only choose one
                        field = frontmatter['field'][0]

                        frontmatter['color'] = field_color_map[field]
                        frontmatter['field_url'] = frontmatter['target_url'].split(field)[0]+f'{field}/'

                        icon_file = f"{custom_dir}/templates/{field}-icon.html"
                        if os.path.exists(icon_file):
                            with open(icon_file, 'r') as iconfile:
                                icon_text = iconfile.read()
                        frontmatter['icon'] = icon_text

                    if 'custom_color' in frontmatter:
                        if frontmatter['custom_color'] in colors:
                            frontmatter['color'] = frontmatter['custom_color']

                    # Do this for different types of units
                    if 'type' in frontmatter:
                        if frontmatter['type'] == 'unit':
                            template = environment.get_template("unit-item.html")
                        else:
                            template = environment.get_template("sensor-item.html")

                            # Firmware is hardcoded - TODO
                            firmware_repo = 'https://github.com/fablabbcn/smartcitizen-kit-2x/releases/tag/'

                            if 'versions' in frontmatter:
                                if 'firmware' in frontmatter['versions']:
                                    frontmatter['firmware_url'] = f"{firmware_repo}{frontmatter['versions']['firmware'].replace('+', '')}"

                            if 'target' in frontmatter:
                                metric = frontmatter['target'][0]
                                frontmatter['metric_url'] = frontmatter['field_url']+f'{metric}/'

                    if DEBUG:
                        print ('\tFrontmatter')
                        print (f'\t{frontmatter}')
                    result = template.render(frontmatter)

                    html_path = os.path.join(f"{custom_dir}/aux", file.replace('.md', '.html')).replace("index", frontmatter['name'].lower().replace(" ","_"))
                    if DEBUG: print (f'\tCreating card {html_path}')

                    with open(html_path, 'w', encoding='utf-8') as _file:
                        _file.write(result)
                    if DEBUG: print ('--DONE--')
    return ''

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

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
    def get_content(filename):

        lines = get_file(filename)

        if '---\n' in lines:
            content = '\n'.join(lines[lines[1:].index('---\n')+1:])
        else:
            content = lines

        return content

    @env.macro
    # Inspired by function in mkdocs-snippets-plugin
    def get_snippet_git(git_url, file_path, section_name, ignore_frontmatter = True):
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
            if ignore_frontmatter:
                result = remove_frontmatter(result)

            return result
        else:
            return "Markdown section doesn't exist in source"

    @env.macro
    # Inspired by function in mkdocs-snippets-plugin
    def get_snippet_url(url, section_name, ignore_frontmatter = True):
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
                if ignore_frontmatter:
                    result = remove_frontmatter(result)
            else:
                result = None

            return result
        else:
            return "Markdown section doesn't exist in source"

    @env.macro
    # Inspired by function in mkdocs-snippets-plugin
    def get_snippet_rel(file_path, section_name = None, ignore_frontmatter = True):

        ok_to_go = False
        try:
            with open(env.project_dir + '/' + file_path, 'r') as myfile:
                content = myfile.read()
        except:
            print (f'Error found while rendering file: {env.page.file.src_uri}')
            print (f"Can't find {env.project_dir + '/' + file_path}")
            pass
        else:
            ok_to_go = True

        if ok_to_go == False: return None

        if section_name is None:
            extract = content.split('\n')
            if extract[0] == '---':
                # print ('we have frontmatter!')
                if ignore_frontmatter:
                    # print ('remove!')
                    result = '\n'.join(remove_frontmatter(extract))
            else:
                result = '\n'.join(extract[1:])
            return result

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
                    if ignore_frontmatter:
                        result = remove_frontmatter(result)
            else:
                result = None

            return result
        else:
            return "Markdown section doesn't exist in source"

    @env.macro
    def remove_frontmatter(markdown):
        if markdown is not None:
            if '---' in markdown:
                result = markdown[markdown[1:].index('---')+2:]
                return result
            else:
                return markdown
        return None

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

    @env.macro
    # TODO - Cleanup
    def insert_cards(type = "", filter = None, value = list()):
        if DEBUG: print ('********')
        if DEBUG: print ('Insert cards')
        if DEBUG: print (f'Type: {type}')
        if DEBUG: print (f'Filter: {filter}')
        if DEBUG: print (f'Value: {value}')
        if DEBUG: print ('********')
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))
        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("grid.html")

        cards_to_get = []
        source_folder = os.path.join('docs', env.page.url)
        if DEBUG: print ('Source folder:', source_folder)

        for (root,_,files) in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):
                    with open(file_path, 'r') as _file:
                        content = _file.readlines()

                    frontmatter = get_frontmatter(content)
                    if frontmatter is not None:
                        if DEBUG: print (file)

                        if 'name' not in frontmatter:
                            if DEBUG: print (f'ERROR: {file} has no \'name\' in frontmatter!')
                            continue

                        if filter is not None:
                            if filter in frontmatter:
                                item_values = frontmatter[filter]
                            else:
                                if DEBUG: print (f'ERROR: {file} does not have {filter} in frontmatter')
                                continue
                            if DEBUG: print (value, item_values)
                            if any([item_value in value for item_value in item_values]):
                                if DEBUG: print ('adding to get')
                                cards_to_get.append(file.replace('.md', '.html'))
                            if DEBUG: print ('----')
                        else:
                            cards_to_get.append(file.replace('.md', '.html'))
                    else:
                        if DEBUG: print (f'ERROR: {file} has no frontmatter')
                        continue

        if DEBUG: print ('CARDS TO GET')
        if DEBUG: print (cards_to_get)
        if DEBUG: print ('---')

        cards = ''
        if cards_to_get:
            if DEBUG: print ('Adding cards')
            for item in cards_to_get:
                file_path = f"{custom_dir}/aux/{item}"

                if os.path.exists(file_path):
                    if DEBUG: print (f'Adding card: {file_path}')
                    with open(file_path, 'r', encoding='utf-8') as file:
                        card = file.read()
                    if card:
                        cards+=card

        if cards:
            result = template.render(cards=cards,  wide=False)
            return result
        return None

    @env.macro
    def insert_custom_cards(custom_cards = list(), wide_columns = False):
        print ('Insert custom cards')
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))
        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("grid.html")

        source_folder = os.path.join('docs', env.page.url)
        if DEBUG: print ('Source folder:', source_folder)

        cards = ''

        for item in custom_cards:
            file_path = f"{custom_dir}/aux/{item}"
            print (file_path)

            if os.path.exists(file_path):
                if DEBUG: print (f'Adding card: {file_path}')
                with open(file_path, 'r', encoding='utf-8') as file:
                    card = file.read()
                if card:
                    cards+=card

        if cards:
            result = template.render(cards=cards, wide=wide_columns)
            return result
        return None

    @env.macro
    def insert_banner():
        # TODO
        return None

    @env.macro
    # Inspired by function in mkdocs-snippets-plugin
    # TODO - Cleanup once it's final
    def insert_references(file_path, ignore_frontmatter = True):

        ok_to_go = False
        try:
            with open(env.project_dir + '/' + file_path, 'r') as myfile:
                content = myfile.read()
        except:
            if DEBUG: print (f'Error found while rendering file: {env.page.file.src_uri}')
            if DEBUG: print (f"Can't find {env.project_dir + '/' + file_path}")
            pass
        else:
            ok_to_go = True

        if not ok_to_go:
            return None

        extract = content.split('\n')
        references = {}
        if DEBUG: print ('REFERENCES')
        # if DEBUG: print (extract)
        # if DEBUG: print (type(extract))
        # if DEBUG: print ('PAGE CONTENT')
        # if DEBUG: print (env.page.markdown)
        # if DEBUG: print ('-----------')

        for item in extract:
            # if DEBUG: print (item)
            if item.startswith('['):
                # if DEBUG: print ('reference key')
                if item not in references:
                    # if DEBUG: print ('new item')
                    if item in env.page.markdown:
                        # if DEBUG: print ('item in md!')
                        references[item]=extract[extract.index(item)+1]
                else:
                    if DEBUG: print ("WARNING: Duplicated item in references")

        # if DEBUG: print ('references')
        # if DEBUG: print (references)
        result = '\n'.join('{}\n {}'.format(key, value) for key, value in references.items())
        # if DEBUG: print ('result')
        # if DEBUG: print (result)
        if DEBUG: print ('---')
        return result
