n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2 # soma
m = n1 * n2 # multiplicação
d = n1 / n2 # divisão
di = n1 // n2 # divisão inteira
e = n1 ** n2 # potência
d = n1 % n2 # resto da divisão
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.4f}, ', end='')
print(f'A divisão inteira é {di} e a potência é {e}')
print(f'A divisão inteira é {di} e o resto da divisão é {d}')
