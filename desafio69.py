# Desafio 069 – Análise de Dados do Grupo: 
# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre: A) quantas pessoas têm mais de 18 anos; 
# B) quantos homens foram cadastrados; C) quantas mulheres têm menos de 20 anos.​

maior_18 = 0
homens = 0
mulheres_menos_20 = 0

while True:
    try:
        
        idade = int(input("Digite a idade da pessoa ( ou -1 para Sair): "))
        sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()
        if idade == -1:
            print("Saindo do programa...")
            break
        while sexo not in ['M', 'F']:
            print("Sexo inválido. Por favor, digite M ou F.")
            sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()

        if idade > 18:
            maior_18 += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres_menos_20 += 1

        continuar = input("Deseja continuar? (S/N): ").strip().upper()
        while continuar not in ['S', 'N']:
            print("Opção inválida. Por favor, digite S ou N.")
            continuar = input("Deseja continuar? (S/N): ").strip().upper()

        if continuar == 'N':
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

print(f"Total de pessoas com mais de 18 anos: {maior_18}")
print(f"Total de homens cadastrados: {homens}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_20}")

# Exemplo de análise de dados do grupo

# while True:
#     try:
#         idade = int(input("Digite a idade da pessoa (ou -1 para sair): "))
#         if idade == -1:
#             print("Saindo do programa...")
#             break
#         sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()
#         if sexo not in ['M', 'F']:
#             print("Sexo inválido. Por favor, digite M ou F.")
#             continue
#         if 'maior 18' not in locals():
#             maior_18 = 0
#         if 'homens' not in locals():
#             homens = 0
#         if 'mulheres' not in locals():
#             mulheres = 0
#         if idade > 18:
#             maior_18 += 1
#         if sexo == 'M':
#             homens += 1
#         if sexo == 'F' and idade < 20:
#             mulheres += 1
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
#     except Exception as e:
#         print(f"Erro inesperado: {e}")
#     finally:
#         print("Fim do programa.")