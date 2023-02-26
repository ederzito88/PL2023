import fileinput

soma = 0
on = 1
ints_list = []
ops_list = []

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
            ints_list.append(int(c))
        elif(c.isalpha()):
            soma += list_to_int(ints_list)*on
            ints_list = []
            print("not")

    