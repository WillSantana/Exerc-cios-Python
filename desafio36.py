print('Desafio 36 - Aula 12')
print('Aprovando Empréstimo')
print('=-' * 20)
emprestimo = float(input('Digite o Valor do \033[1;31;43mEmprestimo:\033[m R$: '))
salario = float(input('Digite o Valor do Seu \033[1;32;44mSalário:\033[m R$: '))
anos = int(input('Digite em \033[1;34;41mQuantos Anos\033[m Você Quer Pagar a Casa: '))
prestacao = emprestimo / (anos * 12)

cores = {'limpa': '\033[m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'azul': '\033[34m'}

print('=-' * 20)
if prestacao > salario * 0.3:
    print('Emprestimo Negado!')
else:
    print('Emprestimo Aprovado!')
    print(f'Você pagará \033[1;37;43mR${prestacao:.2f}\033[m por mês durante {anos * 12} meses')
print('Fim do Programa')
print('=-' * 20)