p1 = input().lower()
p2 = input().lower()

repetidas = []
for i in p1:
    if i in p2 and i not in repetidas:
        repetidas.append(i)
repetidas = sorted(repetidas)
print(" ".join(repetidas))