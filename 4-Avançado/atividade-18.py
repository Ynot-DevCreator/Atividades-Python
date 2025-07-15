import random
#Simulação de Dados
print("=== Jogo dos Dados ===")
def lancamento():
    return random.randint(1,6)
def lados(n):
    lado=[0] * 6
    for i in range(n):
        valor = lancamento()
        print(f"Lado: {valor}")
        lado[valor -1] +=1
    for i, contagem in enumerate(lado):
        if contagem > 0:
            print(f"O lado {i+1} Saiu: {contagem} {plural(contagem)}")
def plural(contagem): 
    if contagem==1:
        return "vez"
    else:
        return "vezes"
def menu():
    n = int(input('Quantos vezes Deseja Lançar o Dado? '))
    lados(n)
while True:
    menu()
    loop = input('Deseja lançar novamente o Dado? 1-Sim 2-Não\n')
    if loop !="1":
        print("Saindo...")
        break