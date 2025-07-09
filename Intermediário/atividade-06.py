# 6. Contador de Vogais
print("===Contador de Vogais===")
palavra = input('Escreva uma Palavra: ')
def contVogais(string):
    string = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += string.count(i)
    return result

print("A Palavra '"+palavra+"'"+" Possui "
      +str(contVogais(palavra))
      +" Vogais.")
