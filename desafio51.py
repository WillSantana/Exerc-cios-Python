# 51 - Progressão Aritmética: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.​

# # Exemplo de progressão aritmética
# def progressao_aritmetica():
#     primeiro_termo = int(input("Digite o primeiro termo da PA: "))  # Solicita o primeiro termo
#     razao = int(input("Digite a razão da PA: "))  # Solicita a razão
#     termos = 10  # Número de termos a serem exibidos
#     pa = [primeiro_termo + i * razao for i in range(termos)]  # Calcula os termos da PA
#     print("Os primeiros 10 termos da PA são:", pa)  # Exibe os termos da PA
# progressao_aritmetica()  # Chama a função para exibir a PA

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termos = 10
print("Os primeiros 10 termos da PA são:")
for i in range(termos):
    print(primeiro_termo + i * razao, end=" ")
print()

    