import random
# 8. Jogo de Adivinhação
opcao = int(input('\t=== Jogo da Adivinhação ===\n\nEsse é um Jogo de Adivinhação de números.\n'
      +'O programa sorteia um número aleatório (de 1 a 10)\n'
      +' e VOCÊ deve acertar qual é esse número.\n\n\t===Deseja Iniciar O Jogo?===\n\t\t1-Sim 2-Não\n\t============================\n'))
if opcao != 2:
    while True:
        numero = random.randrange(0, 11)
        # print(numero)
        while True:
            resposta = int(input('Qual o seu palpite: '))
            if resposta == numero:
                ganhou = (input("Parabéns!! você acertou o Número Sortido. Deseja Jogar novamente? 1-Sim 2-Não\n"))
                if ganhou != "1":
                    print("Obrigado por Jogar!")
                    exit()
                else:
                    break  
            else:
                perdeu = (input("Infelizmente você errou. Deseja Tentar novamente? 1-Sim 2-Não\n"))
                if perdeu != "1":
                    print(f"O número era {numero}. Obrigado por Jogar!")
                    exit()
