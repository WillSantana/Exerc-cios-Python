# Desafio 057 – Validação de Dados: Crie um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.​


while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper() # Lẽ o sexo 
    if sexo in ['M', 'F']: # Verifica se o sexo é M ou f
        print(f"Sexo {sexo} registrado com sucesso.") # Mensagem de sucesso
    else:
        print("Dados inválidos. Por favor, digite 'M' ou 'F'.")
        continue  # Continua o loop se o dado for inválido
    
    break  # Sai do loop se o dado for válido