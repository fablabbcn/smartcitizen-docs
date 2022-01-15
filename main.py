from urllib.parse import urljoin  # Python3
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

domain = 'docs.smartcitizen.me'
url = f'https://{domain}/'

processed = []
queue = [url]

bad_links = []
callers = dict()

def check_download_file(url):
   downloadable = False

   try:
       headers = requests.head(url).headers
   except:
       failure = True
       pass
   else:
       failure = False
   if failure:
       downloadable = True
       return downloadable
   Content_Length = [value for key, value in headers.items() if key == 'Content-Length']
   if len(Content_Length) > 0:
       Content_Size = ''.join(map(str, Content_Length))
   else:
       Content_Size = 'The content size was not available.'

   Content_Disposition_Exists = bool({key: value for key, value in headers.items() if key == 'Content_Disposition'})
   if Content_Disposition_Exists is True:
       downloadable = 'attachment' in headers.get('Content-Disposition', '')
   else:
       Content_Type = {value for key, value in headers.items() if key == 'Content-Type'}

       compression_formats = ['application/gzip', 'application/vnd.rar', 'application/x-7z-compressed',
                              'application/zip', 'application/x-tar']
       compressed_file = bool([file_format for file_format in compression_formats if file_format in Content_Type])

       image_formats = ['image/bmp', 'image/gif', 'image/jpeg', 'image/png', 'image/svg+xml', 'image/tiff',
                        'image/webp']
       image_file = bool([file_format for file_format in image_formats if file_format in Content_Type])

       text_formats = ['application/rtf', 'text/plain']
       text_file = bool([file_format for file_format in text_formats if file_format in Content_Type])

       if compressed_file is True:
           print('Compressed file')
           print(Content_Size)
           downloadable = True
       elif image_file is True:
           print('Image file')
           print(Content_Size)
           downloadable = True
       elif text_file is True:
           print('Text file')
           print(Content_Size)
           downloadable = True
       elif 'application/pdf' in Content_Type:
           print('PDF file')
           print(Content_Size)
           downloadable = True
       elif 'text/csv' in Content_Type:
           print('CSV File')
           print(Content_Size)
           downloadable = True
   return downloadable

while queue:
    l = queue.pop(0)
    print (l)
    if 'cypress' in l or 'mouser' in l or 'aqmd' in l: continue
    try:
        req = requests.get(l)
    except:
        fail_req = True
        pass
    else:
        fail_req = False

    if fail_req:
        bad_links.append(l)
        processed.append(l)
        continue

    if check_download_file(l):
        print ('File is downloadable, moc')
        processed.append(l)
        continue
    if req.status_code != 200 and req.status_code !=201:
        print (f'Bad link found in {l}. Status code: {req.status_code}')
        bad_links.append(l)
        continue
    if domain not in l:
        print (f'External link {l}, not parsing')
        continue # Avoid exploring every link, only check response

    soup = BeautifulSoup(req.content, 'html.parser')
    links = soup.find_all('a')
    links = [ln.get('href') for ln in links if ln.get('href')]
    to_add = []
    callers[l] = links
    for link in links:
        if link == l: continue

        if link.startswith('http'):
            cl = link
        else:
            if link.startswith('/'):
                cl=urljoin(url, link)
            else:
                cl=urljoin(l, link)

        if cl not in queue and cl not in processed:
            to_add.append(cl)

    queue.extend(to_add)
    processed.append(l)

with open('callers.json', 'w') as f:
    json.dump(callers, f)

with open('bad_links.txt', 'w') as f:
    json.dump(bad_links, f)
