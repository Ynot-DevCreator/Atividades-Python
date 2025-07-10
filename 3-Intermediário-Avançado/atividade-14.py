# 14. Identificar Palíndromos
print("=== Palíndromos ===")

string = (input('Digite uma Palavra que Deseja saber se é um Palíndromo: '))
inversao = ''.join(reversed(string))
invertido = ' '.join(inversao)
if string == inversao:
    print(f"===Esta Palavra é um Palindromo===\nPalavra inserida: {string}\nPalavra Invertida: {invertido}")
else:
    print(f"===Esta Palavra não é um Palíndromo===\nPalavra inserida: {string}\nPalavra Invertida: {invertido}")