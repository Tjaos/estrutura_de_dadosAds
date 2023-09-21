nomes = input().split(",")
intervalo = input().split(" ")

x = int(intervalo[0])
y = int(intervalo[1])

nomesIntervalo = []

for i in range(x, y):
    nomesIntervalo.append(nomes[x])
    x = x + 1

print(",".join(nomesIntervalo))