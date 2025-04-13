#47 - Contagem de pares: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# Exemplo de contagem de números pares

# for i in range(1, 51): 
#     if i % 2 == 0: 
#         print(i, end=' ') 
#         print(" ", end=' ') 
# print()    

# contagem_pares() 
# Exemplo de contagem de números pares
def contagem_pares(): # Função para contar números pares
    for i in range(1, 51): # Loop de 1 a 50
        if i % 2 == 0: # Verifica se o número é par
            print(i, end=' ') # Imprime o número par
    print() # Quebra de linha após a contagem

# Chamando a função para imprimir os números pares
contagem_pares()