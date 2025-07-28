# 50 - Soma dos Pares: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.​

# Exemplo de soma de números pares

def soma_pares():
    soma = 0  # Inicializa a soma
    cont = 0  # Inicializa o contador
    for i in range(6):  # Loop para ler 6 números
        numero = int(input("Digite um número: "))  # Solicita um número ao usuário
        if numero % 2 == 0:  # Verifica se o número é par
            soma += numero  # Adiciona o número à soma
            cont += 1  # Incrementa o contador
    if cont > 0:  # Verifica se houve números pares
        print(f"A soma dos números pares digitados é: {soma} e você informou {cont} números pares")  # Exibe a soma dos números pares
    else:
        print("Nenhum número par foi digitado.")  # Mensagem caso não haja números pares

soma_pares()  # Chama a função para calcular a soma dos números pares