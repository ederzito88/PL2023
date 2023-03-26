import re

import re

f = open('processos.txt','r')
lines = f.readlines()
anos = dict()

for line in lines:
    ano = re.search(r'(\d{4})', line)
    #print(re.search(r'(\d{4})', line)).group(0)
    if ano:
            if ano.group(1) in anos:
                anos[ano.group(1)]+=1
            else:
                anos[ano.group(1)] = 1

print(anos)
    