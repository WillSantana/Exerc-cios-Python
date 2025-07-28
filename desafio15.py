quant = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de km rodados: '))
total = (quant * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {total:.2f}')