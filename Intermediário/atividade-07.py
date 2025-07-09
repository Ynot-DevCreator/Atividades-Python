# 7. Gerador de Tabuada
print("===Gerador de Tabuada===")
numero = int(input('Digite o Número da Tabuada Desejada: '))

multi = 1
print("=== Tabuada do Número "+str(numero)+" ===")
while multi<=10:
    resultado = numero * multi
    print("\t"+str(numero)+" * "+str(multi)+" = "+str(resultado))
    multi+=1
print("===========================")