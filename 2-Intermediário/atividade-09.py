# 9. Fatorial de um Número
print("=== Fatorial de um Número ===")
numero = int(input('Digite um Número para ver seu Fatorial: '))
fatorial = 1
contador = numero
while contador > 1:
    fatorial *= contador
    contador -= 1
print(f"O Fatorial do número {numero}! é {fatorial}")