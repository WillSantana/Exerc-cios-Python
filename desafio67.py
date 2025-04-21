# Desafio 067 – Tabuada v3.0: Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
        n = int(input('Digite um número inteiro para ver sua tabuada (ou -1 para sair): '))
        
        # Verifica se o número é negativo para sair do loop
        print('-' * 20)
        if n < 0:
            print('Número negativo recebido. Encerrando o programa...')
            break
        
        # Exibe a tabuada do número digitado
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')
        print('-' * 20)