#49 - Tabuada v2.0: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.​

# Exemplo de tabuada
def tabuada():
    numero = int(input("Digite um número para ver sua tabuada: "))  # Solicita o número ao usuário
    print(f"Tabuada do {numero}:")  # Exibe a tabuada do número
    for i in range(1, 11):  # Loop de 1 a 10
        print(f"{numero} x {i} = {numero * i}")  # Calcula e exibe o resultado da multiplicação
        
tabuada()  # Chama a função para exibir a tabuada

