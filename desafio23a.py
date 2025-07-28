num = int(input('Digite um número: '))
u = num // 1 % 10 # O operador // é a divisão inteira, ou seja, o resultado é um número inteiro.
d = num // 10 % 10 # O operador % é o resto da divisão inteira.
c = num // 100 % 10 # O operador % é o resto da divisão inteira.
m = num // 1000 % 10 # O operador % é o resto da divisão inteira.
print(f'Analisando o número {num}') # O f-string é uma forma de formatar strings em Python.
print(f'Unidade: {u}') 
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')