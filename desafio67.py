# Desafio 067 – Tabuada v3.0: Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    try:
        n = int(input('Digite um número inteiro para ver sua tabuada (ou -1 para sair): '))
        if n == -1:
            print('Saindo do programa..')
            break
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')
        print('-' * 20)
    except ValueError:
        print('Por favor, digite um número inteiro válido.')