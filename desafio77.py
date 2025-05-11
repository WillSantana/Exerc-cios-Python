# Desafio 077 – Contando Vogais em Tupla
# Crie um programa que tenha uma tupla com várias palavras (sem acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
print('-' * 40)
print(f'{"VOGAIS":^40}')
print('-' * 40)

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vagais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
        print()
print('-' * 40)
print('FIM')