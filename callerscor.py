from urllib.parse import urljoin
import json
url = 'https://docs.smartcitizen.me/'

p = dict()

with open('callers.json', 'r') as f:
    d = json.load(f)
    for key in d.keys():
        p[key] = list()
        for link in d[key]:
            if link.startswith('mailto'): continue
            if link.startswith('http'):
                cl = link
            else:
                cl=urljoin(url, link)
            p[key].append(cl)

with open('callerscor.json', 'w') as fp:
    json.dump(p, fp)
