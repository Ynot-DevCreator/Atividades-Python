frase = "Crie uma função que receba uma lista de números"

count = len(frase)

frase_invertida = []

while count > 0:
    count -= 1
    frase_invertida.append(frase[count])

string_invertida = ''.join(frase_invertida)
print(string_invertida)