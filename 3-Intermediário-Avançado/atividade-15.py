# Mostrar Números primos de 1 A 100
print("===Números Primos de 1 a 100===")
numeros= list(range(1, 101))
for i in numeros: # percorre os numeros de 1 a 100
    p=0
    for j in range(1, i+1):
        if i % j == 0: # se o resto da divisão do "for i" pelo "for j" 
            p+=1 # (que está dentro do range de 1 ao numero atual da iteração) for igual a 0
            # ele adiciona 1 ao p
    if p==2: # se o contador de p for igual a 2 (ou seja, numero primo)
         print(i) #printa o numero com 2 divisões na lista de 1 a 100