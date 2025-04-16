# Desafio 060 – Cálculo do Fatorial: Faça um programa que leia um número qualquer e mostre 
# o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.​

# Exemplo de cálculo de fatorial
while True:
    try:
        n = int(input("Digite um número inteiro para calcular o fatorial (ou -1 para sair): "))
        if n == -1:
            print("Saindo do programa...")
            break
        elif n < 0:
            print("Número inválido. O fatorial não é definido para números negativos.")
        else:
            fatorial = 1
            movimento = []  # Lista para armazenar os números do cálculo
            for i in range(n, 0, -1):  # Loop de n até 1
                fatorial *= i
                movimento.append(str(i))  # Adiciona o número à lista como string
            print(f"{n}! = {' x '.join(movimento)} = {fatorial}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")