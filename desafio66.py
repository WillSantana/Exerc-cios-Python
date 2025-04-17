while True: # Loop infinito para continuar pedindo números
    try:
        num = int(input("Digite um número inteiro (ou 999 para sair): "))
        if num == 999: # Condição de parada
            break 
        if 'contador' not in locals():  # Verifica se 'contador' não existe
            contador = 0
        contador += 1
        if 'soma' not in locals():  # Verifica se 'soma' não existe
            soma = 0
        soma += num
    except ValueError:  # Tratamento de erro para entrada inválida
        print("Entrada inválida. Por favor, digite um número inteiro.")
    except Exception as e:  # Tratamento de erro inesperado
        print(f"Erro inesperado: {e}")
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")

