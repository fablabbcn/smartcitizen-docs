from os import pardir, environ, walk, getcwd
from os.path import join, abspath, dirname, exists, basename
import re
import markdown
import os
from urllib.parse import urlparse
import subprocess
import shutil

assets_spath='assets/images'
path='docs'

def get_full_path(filename):
    return abspath(join(getcwd(), filename))

apath = get_full_path(path)

def get_file(filename):

    if exists(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
    else:
        print ('File doesnt exist!')
        lines = ''

    return lines

def get_imgur_links(content):
    jcontent = '\n'.join(content)
    p = re.compile("!\[.*\]\((.*)\)")
    it = p.finditer(jcontent)
    links = {}

    # Check if it's an URL
    for match in it:
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        is_url = re.match(regex, match.group(1))

        if is_url:
            indices = [i for i, s in enumerate(content) if match.group(0) in s]
            for index in indices:
                links[index] = match
    
    return links

for root, dirs, files in walk(apath):
    for file in files:
        if file.endswith('.md'):
            file_fpath = join(root, file)
            print (f'File path: {file_fpath}')
            print (file)
            file_content = get_file(file_fpath)
            print (file_content)
            file_fixed = []
            replacements = {}
            joined_content = '\n'.join(file_content)
            links = get_imgur_links(file_content)
            print (f'{links}')
            for link in links:
                position = link
                source = links[link].group(1)
                destination = join(get_full_path(join(path,assets_spath)))

                if 'imgur' in source:
                    print ('Imgur evil file!')
                    a = urlparse(source)
                    filename = basename(a.path)
                    print ('Filename:')
                    print (filename)  # Output: 09-09-201315-47-571378756077.jpg
                    print ('Downloading...')
                    print (source)
                    print (destination)
                    if exists(join(destination, filename)):
                        print ('File already exists! Skipping')
                    else:
                        subprocess.call(['wget', '--directory-prefix', destination, source])
                    if exists(join(destination, filename)):
                        print ('Got file!')
                        print (f'Replacing in original file {source}')
                        print (joined_content.index(source))
                        replacement = '/' + join(assets_spath, filename)
                        replacements[source] = replacement
                        print ('Added replacement!')
                        print ('Done!')
                    else:
                        print ('Download failed')
            
            file_fixed = []
            for line in file_content:
                if (any([key in line for key in replacements.keys()])):
                    for word, replacement in replacements.items():
                        line = line.replace(word, replacement)
                    print (line)
                    file_fixed.append(line)
                else:
                    file_fixed.append(line)

            print (f'File final Path: {file_fpath}')
            print (f'File content fixed: {file_fixed}')
            print (f'Backing up original file...')
            shutil.move(file_fpath, file_fpath + '.bak')
            with open(file_fpath, 'w') as file:
                print (''.join(file_fixed))
                file.write(''.join(file_fixed))

                print ('File saved')

