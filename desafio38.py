#38 - Comparando números: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: – O primeiro valor é maior; – O segundo valor é maior; – Não existe valor maior, os dois são iguais.

Pnumero = int(input('Digite o primeiro número inteiro: '))
Snumero = int(input('Digite o segundo número inteiro: '))
comparacao = Pnumero - Snumero
print(f'Os números digitados foram {Pnumero} e {Snumero}')
if comparacao > 0:
    print('O primeiro valor é maior!')
elif comparacao < 0:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')