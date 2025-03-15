# Descrição: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# Solicita o salário do funcionário
salario = float(input('Digite o salario do funcionario R$: '))

# Calcula o aumento baseado no salário
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

# Exibe o novo salário
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora')