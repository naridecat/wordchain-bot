import json


dat = json.loads(open('output.json', 'r', encoding='utf-8').read())

bindat = []
for i in range(len(dat)):
    if len(dat[i]) > 1:
        bindat.append(dat[i])

open('output.json', 'w', encoding='utf-8').write(json.dumps(bindat, ensure_ascii=False))