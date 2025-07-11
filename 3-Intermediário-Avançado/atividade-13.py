# 13. Inverter String
print("=== Inversor de Strings ===")

string = (input('Digite uma Palavra ou Frase que Deseja Inverter: '))
invertido = ''.join(reversed(string))
print(f"Palavra/Frase Invertida: {invertido}")