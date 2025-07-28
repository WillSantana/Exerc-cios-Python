#44 - Gerenciador de pagamentos: Elabore um programa que calcule o valor a ser 
# pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto; 
# – à vista no cartão: 5% de desconto;
# – em até 2x no cartão: preço normal; 
# – 3x ou mais no cartão: 20% de juros.


valor = float(input('Digite o valor a ser pago: R$ '))
print('Escolha a forma de pagamento:')
print('1 - Á vista dinheiro/cheque: 10% de desconto' )
print('2 - Á vista no cartão: 5% de desconto')
print('3 - Em ate 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    print(f'O valor a ser pago é \033[33mR${valor * 0.9:.2f}\033[m')
elif opcao == 2:
    print(f'O valor a ser pago é \033[32mR${valor * 0.95:.2f}\033[m')
elif opcao == 3:
    print(f'O valor a ser pago é \033[34mR${valor:.2f}\033[m')
else:
    print(f'O valor a ser pago é \033[31mR${valor * 1.2:.2f}\033[m')