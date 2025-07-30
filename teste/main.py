# CRUD

# Create -> Adicionar
# Read   -> Visualizar
# Update -> Atualizar
# Delete -> Remover

clients = []

# Função para criar cliente
def create_user(name, email, phone):
    if name == None or email == None or phone == None:
        print("[ERRO] Todos os valores devem ser preenchidos")
        return False
    else:
        user_data = {
            "name": name,
            "email": email,
            "phone": phone
        }
        clients.append(user_data)

# Função para visualizar clientes
def read_users():
    print("Tabela com os clientes")
    for client in clients:
        print(f"Nome: {client['name']} | Email: {client['email']} | Telefone: {client['phone']}")

# Função para atualizar os dados de determinado usuario
def update_user(old_name):
    count = 0
    for client in clients:
        if old_name == client['name']:
            old_data = client
            break
        count += 1
    print("Deixe em branco para pular!")
    new_name = input("Escolha um novo nome: ")
    if new_name == "":
        new_name = old_name
    new_email = input("Escolha o novo email: ")
    if new_email == "":
        new_email = old_data['email']
    new_phone = input("Escolha o novo telefone: ")
    if new_phone == "":
        new_phone = old_data['phone']
    clients[count] = {"name": new_name, "email": new_email, "phone": new_phone}

# Função para deletar usuario
def delete_user(name):
    global clients
    new_clients = []
    for client in clients:
        if name != client['name']:
            new_clients.append(client)
    clients = new_clients


while True:
    print("Escolha uma das opções abaixo: \n 1) Adicionar \n 2) Listar \n 3) Atualizar \n 4) Deletar")
    answer = int(input("[1-4]: "))
    match answer:
        case 1:
            name = input("Cite o nome do usuario: ")
            email = input("Cite o email do usuario: ")
            phone = input("Cite o telefone do usuario: ")
            create_user(name, email, phone)
        case 2:
            read_users()
        case 3:
            user_name = input("Coloque o nome do usuario: ")
            update_user(user_name)
        case 4:
            user_name = input("Coloque o nome do usuario para deletar: ")
            delete_user(user_name)
        case _:
            exit()