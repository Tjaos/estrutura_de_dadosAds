qtdLivros = int(input())
lista = []

for i in range(qtdLivros):
    livro = input().split(",")
    lista.append(livro)

for i in range(qtdLivros):
    print(f"Livro {lista[i][0]} de {lista[i][1]}foi publicado em {lista[i][-1]}")


