#39 - Alistamento militar: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: – Se ele ainda vai se alistar ao serviço militar; – Se é a hora de se alistar; – Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
ano = int(input('Digite o ano de nascimento: '))
idade = 2025 - ano
cores = {'limpa': '\033[m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'azul': '\033[34m'}
if idade < 18:
    print(f'Você tem {idade} anos e {cores["verde"]}ainda não precisa se alistar!{cores["limpa"]}')
elif idade == 18:
    print(f'Você tem {idade} anos e {cores["azul"]}está na hora de se alistar!{cores["limpa"]}')
else:
    print(f'Você tem {idade} anos e {cores["vermelho"]}já passou do tempo de se alistar!{cores["limpa"]}')