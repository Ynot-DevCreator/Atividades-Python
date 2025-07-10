# 10. Calcule a soma de uma lista
print("=== Somador de Lista ===")
lista = []
opcao = int(input('Deseja Adicionar um Número à lista? 1-Sim 2-Não: '))
while True:
    if opcao != 1:
        print("Saindo...")
        break
    else:
        numero = float(input('Digite um Número: '))
        lista.append(numero)
        while True:
            opcao = int(input('Deseja Adicionar mais Números à lista? 1-Sim 2-Não: '))
            if opcao != 1:
                soma = sum(lista)
                print(f"A Soma dos números da lista é {format(soma, '.1f')}")
                exit()
            else:
                break

