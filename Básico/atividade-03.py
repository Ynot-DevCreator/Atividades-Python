# 3. Verificador de Números impares ou pares
print("===Verificador de números Impares ou Pares===")
while (True):
  try:
    numero = int(input('Digite um número: '))
    if (numero % 2 == 0):
      print("O número "+str(numero)+" é par")
      break
    else:
      print("O número "+str(numero)+" é impar")
      break
  except ValueError:
    print("Digite um número válido")