# 5. Conversor de Temperatura
print("===Conversor de Temperatura (de °C pra °F)===")
opcao = float(input('Deseja converter qual tipo de temperatura?\n1-Farenheit\n2-Celsius\n'))
if opcao == 1:
  Tf = float(input('Informe a temperatura em °F: '))
  tempC = (Tf - 32) * 5/9
  print("A temperatura "+str(Tf)+"°F em °C é: "+str(format(tempC, ".2f"))+"°C")  
else:
  Tc = float(input('Informe a temperatura em °C: '))
  tempF =  (Tc * 9/5) + 32
  print("A temperatura "+str(Tc)+"°C em °F é: "+str(format(tempF, ".2f"))+"°F")

