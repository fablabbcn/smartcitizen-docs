import json

with open('bad_links.txt', 'r') as fp:
    bl = json.load(fp)

with open('callerscor.json', 'r') as fp:
    cl = json.load(fp)
megabad = list()
badlinksmap = dict()
for link in bl:
    for s in cl:
        if link in cl[s]:
            if link not in badlinksmap: badlinksmap[link]=list()
            sl = s.split('#')[0].replace('%20', ' ')
            sc = sl.replace('http:','https:')
            if sc not in badlinksmap[link] and f'{sc}/' not in badlinksmap[link]: badlinksmap[link].append(sc)
#    t={s for s in cl if link in  cl[s]}

with open('bad_links_map.json', 'w') as fp:
    json.dump(badlinksmap, fp)

