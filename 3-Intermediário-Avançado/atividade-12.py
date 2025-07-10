# 11. Ordernar números de uma lista
print("=== Ordenador de Lista ===")
lista = []
opcao = int(input('Deseja Adicionar um Número à lista? 1-Sim 2-Não: '))
while True:
    if opcao != 1:
        print("Saindo...")
        break
    else:
        numero = float(input('Digite um Número: '))
        lista.append(numero) # Adiciona números à lista
        while True:
            opcao = int(input('Deseja Adicionar mais Números à lista? 1-Sim 2-Não: '))
            if opcao != 1:
                lista.sort() # Ordena automaticamente os componentes da lista
                print("=== Lista Ordenada dos Números Inseridos (Com valores Únicos) ===")
                listaFormat = set(lista)
                print(listaFormat)
                exit()
            else:
                break # Volta para o Loop anterior