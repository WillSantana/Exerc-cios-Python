#41 - Classificando atletas: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM; – Até 14 anos: INFANTIL; – Até 19 anos: JÚNIOR; – Até 25 anos: SÊNIOR; – Acima de 25 anos: MASTER.
from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nascimento
if idade <= 9:
    print('Categoria \033[31mMIRIM\033[m')
elif idade <= 14:
    print('Categoria \033[32mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria \033[33mJÚNIOR\033[m')
elif idade <= 25:
    print('Categoria \033[mSÊNIOR\033[m')
else:
    print('Categoria \033[34mMASTER\033[m')