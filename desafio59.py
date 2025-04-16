from time import sleep # Importa a biblioteca time para usar a função sleep

# Desafio 059 – Criando um Menu de Opções


# Lendo dois valores iniciais
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

opcao = 0 # Inicializa a variável opcao com 0
# Loop para exibir o menu e processar as opções
# O loop continua até que o usuário escolha a opção 5 (sair)
while opcao != 5:
    print("\nEscolha uma opção:")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")
    opcao = int(input("Digite sua opção: ")) # Lê a opção do usuário

    if opcao == 1: # Soma
        soma = valor1 + valor2 # Calcula a soma dos valores
        print(f"A soma de {valor1} + {valor2} é {soma}.") # Exibe o resultado da soma
    elif opcao == 2: # Multiplicação
        produto = valor1 * valor2 # Calcula o produto dos valores
        print(f"O produto de {valor1} x {valor2} é {produto}.") # Exibe o resultado da multiplicação
    elif opcao == 3: # Maior
        maior = max(valor1, valor2) # Encontra o maior valor
        print(f"O maior valor entre {valor1} e {valor2} é {maior}.") # Exibe o maior valor
    elif opcao == 4: # Novos números
        print("Informe os números novamente:") # Solicita novos números
        valor1 = float(input("Digite o primeiro valor: ")) # Lê o primeiro valor
        valor2 = float(input("Digite o segundo valor: ")) # Lê o segundo valor
    elif opcao == 5: # Sair
        print("Finalizando o programa...") # Mensagem de encerramento
    else:
        print("Opção inválida. Tente novamente.") # Mensagem de opção inválida
    sleep(1)

print("Programa encerrado. Obrigado por usar!")