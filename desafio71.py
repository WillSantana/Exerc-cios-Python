# Desafio 071 – Simulador de Caixa Eletrônico: 
# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado 
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.​

# Simula o funcionamento de um caixa eletrônico

print("=-=" * 15)
print("Bem-vindo ao caixa eletrônico!")
print("=-=" * 15)


valor = int(input("Digite o valor a ser sacado (número inteiro): "))
# Inicializa as cédulas disponíveis
cedulas = [100, 50, 20, 10, 5, 1]
# Inicializa o dicionário para armazenar a quantidade de cédulas
while True:
    
    # Verifica se o valor é negativo ou zero para sair do loop
    if valor < 0:
        print("Valor inválido. O valor deve ser maior ou igual a zero.")
        valor = int(input("Digite o valor a ser sacado (número inteiro): "))
        break
    elif valor == 0:
        print("Valor inválido. O valor deve ser maior que zero.")
        valor = int(input("Digite o valor a ser sacado (número inteiro): "))
        break
    
    
    
    else:
        valor_sacado = valor # Armazena o valor sacado
        cedulas_entregues = {} # Dicionário para armazenar a quantidade de cédulas entregues
        for cedula in cedulas: # Percorre as cédulas disponíveis
            quantidade = valor // cedula # Calcula a quantidade de cédulas
            if quantidade > 0: # Verifica se a quantidade é maior que zero
                cedulas_entregues[cedula] = quantidade # Armazena a quantidade de cédulas no dicionário
                valor -= cedula * quantidade # Atualiza o valor a ser sacado
        print(f"Valor sacado: R$ {valor_sacado}")
        print("Cédulas entregues:")
        for cedula, quantidade in cedulas_entregues.items(): # Percorre o dicionário de cédulas entregues
            print(f"{quantidade} cédula(s) de R$ {cedula}") # Exibe a quantidade de cédulas entregues
        print("=-=" * 15)
        
        # Pergunta se o usuário deseja realizar outro saque
        continuar = input("Deseja realizar outro saque? (S/N): ").strip().upper()
        if continuar == 'N':
            print("Obrigado por usar o caixa eletrônico!")
            break
        elif continuar != 'S':
            print("Opção inválida. Saindo do programa...")
            break