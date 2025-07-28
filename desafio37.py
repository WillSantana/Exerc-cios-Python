# 37 - Conversor de bases numéricas: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
print('Escolha uma base de conversão: ')
print(1, 'para binário')
print(2, 'para octal')
print(3, 'para hexadecimal')
opcao = int(input('sua opçao: '))
if opcao == 1:
    print(f'O número {numero} em binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} em octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} em hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida!')
    