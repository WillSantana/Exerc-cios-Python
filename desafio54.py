# 54 - Grupo da Maioridade: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.​

# repetição laco for
from datetime import date
def grupo_maioridade():
    maioridade = 0 # Inicia a contagem de maiores de idade
    menoridade = 0 # Inicia a contagem de menores de idade
    ano_atual = date.today().year # Obtém o ano atual
    for i in range(1, 8): # Loop para ler os anos de nascimento
        ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: ")) # Lê o ano de nascimento
        idade = ano_atual - ano_nascimento # Calcula a idade
        if idade >= 18: # Verifica se a pessoa é maior de idade
            maioridade += 1 # Incrementa o contador de maiores de idade
        else:
            menoridade += 1 # Incrementa o contador de menores de idade
    return maioridade, menoridade # Retorna os contadores

maioridade, menoridade = grupo_maioridade() # Chama a função e armazena os resultados

print(f"Total de pessoas maiores de idade: {maioridade}") # Exibe o total de maiores de idade
print(f"Total de pessoas menores de idade: {menoridade}") # Exibe o total de menores de idade

