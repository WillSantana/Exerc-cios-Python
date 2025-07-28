# 53 - Detector de Palíndromo: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços.​

frase = str(input("Digite uma frase: ")).strip().upper()  # Solicita uma frase e remove espaços
palavras = frase.split()  # Divide a frase em palavras
junto = ''.join(palavras)  # Junta as palavras em uma única string
inverso = ''  # Inverte a string
for i in range(len(junto) -1, -1, -1):  # Loop para inverter a string
    inverso += junto[i]  # Adiciona cada caractere invertido à nova string
print(f"O inverso de {junto} é {inverso}")  # Exibe a string invertida
# Verifica se a string original é igual à string invertida
if inverso == junto:  # Compara a string original com a invertida
    print("A frase digitada é um palíndromo.")  # Mensagem se for palíndromo
else:
    print("A frase digitada não é um palíndromo.")  # Mensagem se não for palíndromo


# função 
# Exemplo de palíndromo
# def palindrome():
#     frase = input("Digite uma frase: ").replace(" ", "").lower()  # Solicita uma frase e remove espaços
#     if frase == frase[::-1]:  # Verifica se a frase é igual à sua inversa
#         print("A frase é um palíndromo.")  # Mensagem se for palíndromo
#     else:
#         print("A frase não é um palíndromo.")  # Mensagem se não for palíndromo
# palindrome()  # Chama a função para verificar o palíndromo
