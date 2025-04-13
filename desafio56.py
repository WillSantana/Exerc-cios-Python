# 56 - Analisador Completo: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo; qual é o nome do homem mais velho; 
# quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for i in range(1, 5):
    print ( f'-------- {i}ª PESSOA --------')
    nome = str(input(f"Digite o nome da {i}ª pessoa: "))  # Lê o nome
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))  # Lê a idade
    sexo = str(input(f"Digite o sexo da {i}ª pessoa (M/F): ")).strip().upper()  # Lê o sexo
    somaidade += idade # Soma a idade ao total
    
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho =  nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    mediaidade = somaidade /4
    print(f"Média de idade do grupo: {mediaidade:.2f}") # Exibe a média de idade
    print(f"Homem mais velho: {nomevelho}") # Exibe o nome do homem mais velho
    print(f"Quantidade de mulheres com menos de 20 anos: {totmulher20}") # Exibe a quantidade de mulheres com menos de 20 anos


# funçao 

# def analisador_completo():
#     total_idade = 0
#     homens = []
#     mulheres_menores_20 = 0
    
#     for i in range(4):  # Loop para ler os dados de 4 pessoas
#         print (f'-------- {i}ª PESSOA --------')
#         nome = input(f"Digite o nome da {i + 1}ª pessoa: ")  # Lê o nome
#         idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))  # Lê a idade
#         sexo = input(f"Digite o sexo da {i + 1}ª pessoa (M/F): ").strip().upper()  # Lê o sexo
        
#         total_idade += idade  # Soma a idade ao total
        
#         if sexo == 'M':  # Verifica se é homem
#             homens.append((nome, idade))  # Adiciona o homem à lista
#         elif sexo == 'F' and idade < 20:  # Verifica se é mulher e menor de 20
#             mulheres_menores_20 += 1  # Incrementa o contador de mulheres menores de 20
            
#     media_idade = total_idade / 4  # Calcula a média de idade
#     homem_mais_velho = max(homens, key=lambda x: x[1])[0] if homens else "Nenhum homem"  # Encontra o homem mais velho
    

#     print(f"Média de idade do grupo: {media_idade:.2f}") # Exibe a média de idade
#     print(f"Homem mais velho: {homem_mais_velho}") # Exibe o nome do homem mais velho
#     print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menores_20}")

# # Chama a função
# analisador_completo()  # Chama a função para executar o programa