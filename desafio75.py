# Desafio 075 – Análise de Dados em uma Tupla: 
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 
# A) quantas vezes apareceu o valor 9; 
# B) em que posição foi digitado o primeiro valor 3; 
# C) quais foram os números pares

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))
valores = (valor1, valor2, valor3, valor4)

print(f"Você digitou os valores: {valores}")
# A) quantas vezes apareceu o valor 9
quantas_vezes_9 = valores.count(9)
print(f"O valor 9 apareceu {quantas_vezes_9} vezes.")
# B) em que posição foi digitado o primeiro valor 3
if 3 in valores:
    posicao_primeiro_3 = valores.index(3) + 1
    print(f"O primeiro valor 3 foi digitado na posição {posicao_primeiro_3}.")
else:
    print("O valor 3 não foi digitado. ")
# C) quais foram os números pares
numeros_pares = [valor for valor in valores if valor % 2 == 0]
if numeros_pares:
    print(f"Os números pares digitados foram: {numeros_pares}")
else:
    print("Nenhum número par foi digitado.")

