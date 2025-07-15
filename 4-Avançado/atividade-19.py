import random
import string
#Sistema de Cadastro de Clientes
print("=== Sistema de Cadastro de Clientes ===")
def cadastroCliente(cliente, id):
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('Email: ')
    
    cliente[id] = {
        "Nome": nome,
        "Telefone": telefone,
        "email": email
    }

def visualizarLista(cliente):
    for id, dados in cliente.items():
        print(f"\nID: {id}")
        print(f"Nome: {dados['Nome']}")
        print(f"Telefone: {dados['Telefone']}")
        print(f"Email: {dados['email']}")

def menu():
    print('''\n       === Menu de Opções ===
====================================
1- Cadastro de Cliente
2- Visualizar Clientes Cadastrados
3- Remover Cliente Cadastrado
4- Sair
====================================\n''')

clientes = {}
identificador = 1

def removerCliente(cliente):
    visualizarLista(cliente)
    deletar = int(input('Qual Cliente Deseja Remover? (Remoção por ID)\n'))
    try: 
        del cliente[deletar]
    except KeyError:
        print("ERRO: Cliente não encontrado ID inválido")

while True:
    menu()
    opcao = int(input('Opção Desejada: '))
    match opcao:
        case 1:
            cadastroCliente(clientes, identificador)
            identificador+=1
        case 2:
            visualizarLista(clientes)
        case 3:
            removerCliente(clientes)
        case 4:
            print("Encerrando Sistema...")
            exit()