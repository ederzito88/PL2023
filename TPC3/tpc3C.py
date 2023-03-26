import re

file = open("processos.txt", "r")
dict_relacoes = dict()
for line in file:
    r = re.match(r"\d+::(?P<ano>\d+)-\d{2}-\d{2}::([A-Z][a-z]*) ([A-Z][a-z]* ){0,}([A-Z][a-z]*)", line)
    fall_relacoes = re.findall(r",([a-zA-z]+)((?: +[a-zA-z]+)*)\. +Proc.\d+\.", line)
    
    if r is not None:  
        for match in fall_relacoes:
            rel = ''
            for p in match:
                rel += p
            
            if rel in dict_relacoes:
                dict_relacoes[rel] += 1
            else:
                dict_relacoes[rel] = 1
                    
file.close()
print (dict(sorted(dict_relacoes.items(), key=lambda x: x[1], reverse=True)))