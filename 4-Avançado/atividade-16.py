import random
# Jogo da Forca
print("=== Jogo da Forca ===")

palavras = ["Bandeira", "Abacaxi", "Computador", "Simulação", "Palíndromo", "Repositório", "Relâmpago", "Algoritmo", "Guaxinim", "Ornitorrinco"]

bonecocompleto = '''  
     _________
     |       |
     |       O
     |      /|\\
     |      / \\
    _|_'''
print(bonecocompleto)
while True:
    opcao = int(input("Deseja Iniciar o Jogo? 1-Sim 2-Não"))
    if opcao !=1:
        break
    else:
        pEscolhida = random.choice(palavras)
        oculta = ' _' * len(pEscolhida)
        print(oculta)
