nomes = ["Anna", "Bruno", "Carlos", "Diana", "Eduardo"]
for nome in nomes:
    print(f"Olá, {nome}! Seja bem-vindo(a) ao curso de Python.")
    
    
#-------------------------------------------
# percorra uma lista de numeros e imprima

numeros = [1, 3, 5, 7, 10, 12, 15, 20]
for numero in numeros:
    print(f"O número {numero} e o Quadrado é {numero * 2}  ")
    
    
#-------------------------------------------
# Filtre apenas os números pares dentro do for
for numero in numeros:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
        