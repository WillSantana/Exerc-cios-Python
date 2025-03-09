from random import choice
# choice(seq): Retorna um elemento aleatório de uma sequência não vazia.
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
print(f'O aluno escolhido foi {choice([aluno1, aluno2, aluno3, aluno4])}')
