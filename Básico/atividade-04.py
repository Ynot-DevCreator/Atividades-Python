#############
# Básico
#############

# 4. Calcular Média de Notas
print("===Calculador de média de Notas===")
aluno = input('Informe o nome do Aluno(a): ')
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
n4 = float(input('Informe a quarta nota: '))

media = (n1 + n2 + n3 + n4)/4

print("A média do Aluno(a) "+aluno+" é: "+str(media))