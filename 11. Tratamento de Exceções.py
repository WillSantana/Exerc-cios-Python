try:
    numero = int(input("Digite um número: "))
    print(100 / numero)
except ZeroDivisionError:
    print("Divisão por zero!")
except ValueError:
    print("Valor inválido! Digite um número inteiro.")
else:
    print("Operação realizada com sucesso.")