import matplotlib.pyplot as plot

file = open("myheart.csv")
next(file)
# f.readlines()
data = []

for line in file:
  #line = line.strip()
  values = line.split(',')
  tuple = (
      int(values[0]),
      values[1],
      int(values[2]),
      int(values[3]),
      int(values[4]),
      bool(int(values[5]))
  )
  data.append(tuple)
  
#print(data)


def distbyS():
  ddistbyS = {'M': {'com_doenca': 0, 'sem_doenca': 0}, 'F': {'com_doenca': 0, 'sem_doenca': 0}}
  for _,sexo, _, _, _, tem_doenca in data:
        if tem_doenca:
            ddistbyS[sexo]['com_doenca'] += 1
        else:
            ddistbyS[sexo]['sem_doenca'] += 1

  #print(ddistbyS)
  dict2 = {'M com doença': ddistbyS["M"]["com_doenca"],'M sem doença': ddistbyS["M"]["sem_doenca"],'F com doença': ddistbyS["F"]["com_doenca"],'F sem doença': ddistbyS["F"]["sem_doenca"]}
  printDistribution(dict2,"Sexo", "fa")
  
def distbyEsc():
  
  ddistbyEsc = dict()
  maior = None
  menor= 30

  for tuple in data:
      idade = tuple[0]
      interval_idade = (idade//5*5, (idade//5+1)*5-1)
      if interval_idade not in ddistbyEsc:
          ddistbyEsc[interval_idade] = 1
      else:
          ddistbyEsc[interval_idade] += 1
      
      if interval_idade[0] < menor:
          menor = interval_idade[0]
      
      if maior is None:
          maior = interval_idade[0]
      elif interval_idade[0] > maior:
          maior = interval_idade[0]
  
  if maior is not None:
      i = menor
      while i<=maior:
          if (i,i+4) not in ddistbyEsc:
              ddistbyEsc[(i,i+4)] = 0
          i+=5
          
  #print(sorted(ddistbyEsc.items()))
  printDistribution(ddistbyEsc,"Idades", "fa")     
  
  
def distbyCol():
  colestrol_min, colestrol_max = min([row[3] for row in data]),max([row[3] for row in data])
  ddbyCol = dict()
  
  i=colestrol_min
  while i<=colestrol_max:
      ddbyCol[(i,i+9)] = 0
      i+=10
  
  for tuple in data:
      colestrol = tuple[3]
      int_colestrol = (colestrol_min+(colestrol-colestrol_min)//10*10, colestrol_min+((colestrol-colestrol_min)//10+1)*10-1)
      if int_colestrol not in ddbyCol:
          ddbyCol[int_colestrol] = 1
      else:
          ddbyCol[int_colestrol] += 1
              
  #print(sorted(ddbyCol.items()))  
  printDistribution(ddbyCol,"Níveis", "fa")

def printDistribution(someDict,table_key,table_value):
    keys = list(someDict.keys())
    values = list(someDict.values())

    # To prevent the case when we have diferent length
    max_key_length = max([len(str(key)) for key in keys])
    max_value_length = max([len(str(value)) for value in values])

    if max_key_length < len(table_key): max_key_length = len(table_key)
    if max_value_length < len(table_value): max_value_length = len(table_value) 

    # Header of the table
    print(f"\n+{'-' * (max_key_length + 2)}-{'-' * (max_value_length + 2)}+")
    print(f"| {table_key.ljust(max_key_length)} | {table_value.ljust(max_value_length)} |")
    # Print the tabel
    for i in range(len(keys)):
        print(f"|{'-' * (max_key_length + 2)}|{'-' * (max_value_length + 2)}|")
        print(f"| {str(keys[i]).ljust(max_key_length)} | {str(values[i]).ljust(max_value_length)} |")
    print(f"+{'-' * (max_key_length + 2)}-{'-' * (max_value_length + 2)}+")

def grafico_barras(titulo, eixo_x, eixo_y, data):
    x_values = [str(key) for key in data.keys()]
    y_values = data.values()
    
    barras = plot.bar(x_values, y_values)
    plot.bar_label(barras, labels=y_values)

    manager = plot.get_current_fig_manager()
    manager.set_window_title(titulo)

    plot.title(titulo)
    plot.xlabel(eixo_x)
    plot.ylabel(eixo_y)
    
    plot.show()

distbyS()
distbyEsc()
distbyCol()
