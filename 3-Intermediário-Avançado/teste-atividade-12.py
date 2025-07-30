lista = ['Maçã', "Melancia", "Abacaxi", "Pera", "Melancia", "Banana", "Goiaba", "Banana", "Goiaba", "Goiaba", "Pera", "Melancia"]
lista_final = []

for fruta in lista:
    if fruta not in lista_final:
        lista_final.append(fruta)

print(lista_final)