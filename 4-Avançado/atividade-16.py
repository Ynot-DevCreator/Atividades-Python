import random
# Jogo da Forca
print("=== Jogo da Forca ===")

palavras = ["Bandeira", "Abacaxi", "Computador", "Simulação", "Palíndromo", "Repositório", "Relâmpago", "Algoritmo", "Guaxinim", "Ornitorrinco"]
letras_usuario = []
chances = 6
erros = 0
bonecos = ['''  
     _________
     |       |
     |       
     |      
     |      
    _|_
''', '''  
     _________
     |       |
     |       O
     |      
     |      
    _|_
''', '''  
     _________
     |       |
     |       O
     |       |
     |      
    _|_
''', '''  
     _________
     |       |
     |       O
     |      /|
     |      
    _|_
''', '''  
     _________
     |       |
     |       O
     |      /|\\
     |      
    _|_
''', '''  
     _________
     |       |
     |       O
     |      /|\\
     |      / 
    _|_
''', '''  
     _________
     |       |
     |       O
     |      /|\\
     |      / \\
    _|_
''']
ganhou = False  
# print(bonecos[0])
pEscolhida = random.choice(palavras)
while True:
        for letra in pEscolhida.lower():
            if letra.lower() in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print(f"\nVocê tem {chances} chances\n\t {bonecos[erros]}")
        tentativa = input("Escolha uma letra para Adivinhar: ")
        letras_usuario.append(tentativa.lower())
        if tentativa.lower() not in pEscolhida.lower():
            chances -= 1
            erros += 1
        ganhou = True
        for letra in pEscolhida:
            if letra.lower() not in letras_usuario:
                ganhou = False
        if chances == 0 or ganhou:
            break
if ganhou:
    print(f"Parabéns Você Ganhou!! A palavra era: {pEscolhida}")
else:
    print(f"Você Perdeu! A palavra era: {pEscolhida}\n{bonecos[-1]}")