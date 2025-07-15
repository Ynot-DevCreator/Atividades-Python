import random
import string
# Gerador de Senhas
print("=== Gerador De Senhas Aleatórias===")
Password = ""
while True:
    opcao = int(input('Qual nível de Segurança de Senha Deseja?\n==========\n1-Fraca\n2-Média\n3-Forte\n==========\n'))
    match opcao:
        case 1:
            Password = ''.join(random.choices(string.digits, k=8))
            print("Senha Fraca Gerada: "+str(Password))       
        case 2:
            Password = ''.join(random.choices(string.digits + string.ascii_letters, k=10))
            print("Senha Média Gerada: "+str(Password))
        case 3:
            Password = ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation, k=12))
            print("Senha Forte Gerada: "+str(Password))
    loop = input("Deseja Criar Outra Senha? 1-Sim 2-Não\n")
    if loop != "1":
        print("Saindo...")
        break