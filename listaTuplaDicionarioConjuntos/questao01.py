hortfrut = ("banana", 15, "maçã", 16, "pêra", 10, "uva", 6, "melancia", 30, "cebola", 45, "alho", 12, "tomate", 13, "cenoura", 18, "pimentão", 4)

fruta = input("Digite o nome da fruta desejada: ")

while fruta not in hortfrut:
        if fruta == "":
                continue
        print("Digite o nome da fruta corretamente!")
        fruta = input("Digite o nome da fruta desejada: ")

print (f"A quantidade de {fruta} no estoque é: {hortfrut[hortfrut.index(fruta)+1]}") 


