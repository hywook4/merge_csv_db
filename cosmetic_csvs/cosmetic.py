import csv
import sys

csvfile = sys.argv[1]


dblist = open('dbcosmetic.csv', encoding="utf8")
l = csv.reader(dblist)
writelist = list(l)


dblist.close()


f = open(csvfile)
r = csv.reader(f)
readlist = list(r)

f.close()



newlist = []

index = {
    'name': None,
    'brand': None,
    'category': None,
    'component': None
}

for row in range (0, len(readlist)):
    for column in range(0, len(readlist[row])):
        tag = readlist[row][column]

        if '제품' in tag and '명' in tag:
            index['name'] = [row, column+1]
        elif '브랜드' in tag:
            index['brand'] = [row, column+1]
        elif '카테고리' in tag:
            index['category'] = [row, column+1]
        elif '성분명' in tag:
            index['component'] = [row+1, column] 

for k, v in index.items():
    if k != 'component':
        newlist.append(readlist[v[0]][v[1]])
    
    else:
        if v == None:
            newlist.append('')
        elif v[0] >= len(readlist):
            newlist.append('')
        else:
            components = readlist[v[0]][v[1]]
            for i in range (v[0]+1, len(readlist)):
                if readlist[i][v[1]] != '':
                    components += ";" + readlist[i][v[1]]
            
            newlist.append(components)



writelist.append(newlist)

'''
for a in writelist:
    print(a)
'''

with open('dbcosmetic.csv', 'w') as w:
    writer = csv.writer(w)
    writer.writerows(writelist)

w.close()


