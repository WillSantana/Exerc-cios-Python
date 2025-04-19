total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = None

while True:
    try:
        nome = input("Digite o nome do produto (ou 'Sair' para sair): ")
        if nome.lower() == 'sair':
            break
        preco = float(input("Digite o preço do produto: R$ "))
        if preco < 0:
            print("Preço inválido. O preço deve ser maior ou igual a zero.")
            continue

        total_gasto += preco
        if preco > 1000:
            produtos_acima_1000 += 1
        if produto_mais_barato is None or preco < produto_mais_barato[1]:
            produto_mais_barato = (nome, preco)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para o preço.")
        continue

    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar == 'N':
        break

print(f"Total gasto na compra: R$ {total_gasto:.2f}")
print(f"Total de produtos acima de R$ 1000: {produtos_acima_1000}")
if produto_mais_barato:
    print(f"Produto mais barato: {produto_mais_barato[0]} - R$ {produto_mais_barato[1]:.2f}")
else:
    print("Nenhum produto foi cadastrado.")

#
# Exemplo de estatísticas em produtos
# total_gasto = 0
# produtos_acima_1000 = 0
# produtos_com_mais_barato = None

# while True:
#     try:
#         nome = input("Digite o nome do produto (ou 'Sair' para sair): ")
#         if nome.lower() == 'sair':
#             print("Saindo do programa...")
#             break
#         preco = float(input("Digite o preço do produto: R$ "))
#         if preco < 0:
#             print("Preço inválido. O preço deve ser maior ou igual a zero.")
        
        
#         if preco > 1000:
#             produtos_acima_1000 += 1
#         total_gasto += preco
#         if produtos_com_mais_barato is None or preco < produtos_com_mais_barato[1]:
#             produtos_com_mais_barato = (nome, preco)
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número válido para o preço.")
#     except Exception as e:
#         print(f"Erro inesperado: {e}")
#     finally:
#         print("Fim do programa.")
    
        
        
#         continuar = input("Deseja continuar? (S/N): ").strip().upper()
#         if continuar not in ['S', 'N']:
#             print("Opção inválida. Por favor, digite S ou N. ")
#             continue
#         if continuar == 'N':
#             break
    
#     print(f"Total gasto na compra: R$ {total_gasto:.2f}")
#     print(f"Total de produtos acima de R$ 1000: {produtos_acima_1000}")
#     if produtos_com_mais_barato:
#         print(f"Produto mais barato: {produtos_com_mais_barato[0]} - R$ {produtos_com_mais_barato[1]:.2f}")
#     else:
#         print("Nenhum produto foi cadastrado.")

        