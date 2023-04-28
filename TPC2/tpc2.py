import fileinput

print('--Insira uma sequência de dígitos')
print('--O contador está ligado')

soma = 0
on = 1
ints_list = []
ops_list = []

#Transforma uma lista de inteiros no nr inteiro formado pela sua concatenação
def list_to_int(list):
    if list: return int(''.join(map(str, list)))
    else: return 0

for line in fileinput.input():
    #parse_line(line)
    #print(type(line))
    for c in line:
        if (c == '='):
            soma += list_to_int(ints_list)*on
            ints_list = []
            print(soma)
        elif (c.isdigit()):
            ops_list = []
            ints_list.append(int(c))
        elif(c.isalpha()):
            soma += list_to_int(ints_list)*on
            ints_list = []
            #print("not")
            if (c.lower() in ['o','f','n']): 
                if (c.lower() == 'o'): ops_list = []
                ops_list.append(c)
                #print(''.join(ops_list).lower())
                if (''.join(ops_list).lower()) == 'off':
                    on = 0
                    #print('desliguei')
                    ops_list = []
                if (''.join(ops_list).lower()) == 'on':
                    on = 1
                    #print('liguei')
                    ops_list = []
    if (''.join(ops_list).lower()) not in ['off','on','o', 'of']:  ops_list = []

    