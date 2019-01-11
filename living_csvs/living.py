import csv
import sys
   
csvfile = sys.argv[1]


dblist = open('dbliving.csv', encoding="utf8")
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
    'manufacture': None,
    'category': None,
    'ingredient_open': None,
    'check_number': None,
    'permission_state': None,
    'ecofriendly_state': None,
    'global_state' : None,
    'component_index':None
}

for row in range (0, len(readlist)):
    for column in range(0, len(readlist[row])):
        tag = readlist[row][column]

        if '제품' in tag and '이름' in tag:
            index['name'] = [row+1, column]
        elif '브랜드' in tag:
            index['brand'] = [row, column+1]
        elif '제조사' in tag:
            index['manufacture'] = [row, column+1]
        elif '카테고리' in tag:
            index['category'] = [row, column+1]
        elif '성분' in tag and '공개' in tag:
            index['ingredient_open'] = [row, column+1]
        elif '자가' in tag and '검사' in tag:
            index['check_number'] = [row, column+1]
        elif '기타' in tag and '허가' in tag and '인증' in tag:
            index['permission_state'] = [row, column+1]
        elif '친환경' in tag and '인증' in tag:
            index['ecofriendly_state'] = [row, column+1]
        elif '해외' in tag and '인증' in tag:
            index['global_state'] = [row, column+1]
        elif '고유' in tag and '번호' in tag:
            index['component_index'] = [row+1, column]

for k, v in index.items():
    if k != 'component_index':
        #print(readlist[v[0]][v[1]])
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
                    components += ";"+readlist[i][v[1]]

            #print(components)
            newlist.append(components)



writelist.append(newlist)

'''
for a in writelist:
    print(a)
'''

with open('dbliving.csv', 'w') as w:
    writer = csv.writer(w)
    writer.writerows(writelist)

w.close()



