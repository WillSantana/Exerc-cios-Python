# Desafio 078 – Maior e Menor Valores na Lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


valores = []

for i in range(5):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    valores.append(valor)
    
maior = max(valores)
menor = min(valores)
posicao_maior = valores.index(maior)

print(f'O maior valor digitado foi {maior} na posição {posicao_maior}.')
print(f'O menor valor digitado foi {menor} na posição {valores.index(menor)}.')
print(f'A lista completa é: {valores}')
