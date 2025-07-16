# 20. Calculadora de Média de Números em Arquivo
# ==============================================
# Variáveis

arquivoTxt = "C:\\Users\Aluno\\Desktop\\Atividades python\\4-Avançado\\listaNumeros.txt"
cont = 0
soma = 0
# ==============================================

print('''=== Calculadora de Média de Números em Arquivo ===

=================================
Lista de Números''')
with open(arquivoTxt, "r", encoding="UTF-8") as arquivo:
    linhas = arquivo.readlines()
    for i in linhas:
        i = float(i.strip())
        print(f"{i}")
        soma+=i
        cont+=1
    media = soma/cont
    print(f'''=================================
          
=================================
Quantidade de Números: {cont}
Média dos Numeros da lista: {format(media, '.1f')}
=================================''')