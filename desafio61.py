 # Desafio 061 – Progressão Aritmética v2.0: Refaça o DESAFIO 51, lendo o primeiro termo 
 # e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a
 # estrutura while.
 
# Exemplo de execução:
print("=-=" * 10 ) 
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termos = 10
contador = 1
print("Os primeiros 10 termos da PA são:")
while contador <= termos:
    print(primeiro_termo, end=" ")
    primeiro_termo += razao
    contador += 1
print()
