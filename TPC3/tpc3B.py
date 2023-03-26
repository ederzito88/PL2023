import re

file = open("processos.txt", "r")
dict_pnomes = dict()
dict_apelidos = dict()

for line in file:
    m_ano = re.match(r"\d+::(?P<ano>\d+)-\d{2}-\d{2}::([A-Z][a-z]*) ([A-Z][a-z]* ){0,}([A-Z][a-z]*)", line)
    fall_nomes = re.findall(r"::([A-Z][a-z]*) ([A-Z][a-z]* ){0,}([A-Z][a-z]*)", line)
    
    if m_ano is not None and fall_nomes is not None:
        ano = int(m_ano.group('ano'))
        seculo = (ano - 1) // 100 + 1
        fall_nomes = fall_nomes[:3]
        for match in fall_nomes:
            primeiro_nome = match[0]
            apelido = match[-1]
            
            if seculo in dict_pnomes:
                if primeiro_nome in dict_pnomes[seculo]:
                    dict_pnomes[seculo][primeiro_nome] += 1
                else:
                    dict_pnomes[seculo][primeiro_nome] = 1
            else:
                dict_pnomes[seculo] = dict()
                dict_pnomes[seculo][primeiro_nome] = 1
                
            if seculo in dict_apelidos:
                if apelido in dict_apelidos[seculo]:
                    dict_apelidos[seculo][apelido] += 1
                else:
                    dict_apelidos[seculo][apelido] = 1
            else:
                dict_apelidos[seculo] = dict()
                dict_apelidos[seculo][apelido] = 1     

file.close()

dict_pnomes = dict(sorted(dict_pnomes.items(), reverse=True))
for seculo in dict_pnomes:
    dict_pnomes[seculo] = dict(sorted(dict_pnomes[seculo].items(), key=lambda x: x[1], reverse=True))

dict_apelidos = dict(sorted(dict_apelidos.items(), reverse=True))
for seculo in dict_apelidos:
    dict_apelidos[seculo] = dict(sorted(dict_apelidos[seculo].items(), key=lambda x: x[1], reverse=True))
print (dict_pnomes, dict_apelidos)
