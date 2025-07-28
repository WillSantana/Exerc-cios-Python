print("{:=^40}".format(" LOJAS PYTHON "))
preco = float(input("Preço das compras: R$ "))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = preco - (preco * 0.10)
    print("Você ganhou 10% de desconto!")
elif opcao == 2:
    total = preco - (preco * 0.05)
    print("Você ganhou 5% de desconto!")
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.")
elif opcao == 4:
    total = preco + (preco * 0.20)
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print(f"Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f} COM JUROS.")
else:
    total = preco
    print("Opção inválida de pagamento. Tente novamente!")

print(f"Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final.")