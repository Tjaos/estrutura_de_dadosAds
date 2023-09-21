numeros = input().split(" ")

listaMae = [[],[]]

i=0
for i in range((len(numeros))):
    if int(numeros[i])%2==0:
        listaMae[0].append(int(numeros[i]))
    else:
        listaMae[1].append(int(numeros[i]))
    i=i+1

listaMae[0] = sorted(listaMae[0])
listaMae[1] = sorted(listaMae[1])
print(f"{listaMae}")


#print(type(int(numeros[0])))