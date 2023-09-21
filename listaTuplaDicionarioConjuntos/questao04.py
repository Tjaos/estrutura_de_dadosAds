numeros = input().split(" ")

pares = []
impares = []

i=0
for i in range((len(numeros))):
    if int(numeros[i])%2==0:
        pares.append(int(numeros[i]))
    else:
        impares.append(int(numeros[i]))
    i=i+1

pares = sorted(pares)
impares = sorted(impares)
print(f"{pares}, {impares}")


#print(type(int(numeros[0])))