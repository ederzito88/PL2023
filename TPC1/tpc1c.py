file = open("myheart.csv")
next(file)
# f.readlines()
list = []

for line in file:
  #line = line.strip()
  valores = line.split(',')
  tuplo = (
      int(valores[0]),
      valores[1],
      int(valores[2]),
      int(valores[3]),
      int(valores[4]),
      bool(int(valores[5]))
  )
  list.append(tuplo)
  
print(list)


def distbyS():
  ddistbyS = {'M': {'com_doenca': 0, 'sem_doenca': 0}, 'F': {'com_doenca': 0, 'sem_doenca': 0}}
  for _, sexo, _, _, _, tem_doenca in list:
        if tem_doenca:
            ddistbyS[sexo]['com_doenca'] += 1
        else:
            ddistbyS[sexo]['sem_doenca'] += 1

  print(ddistbyS)

distbyS()
  
