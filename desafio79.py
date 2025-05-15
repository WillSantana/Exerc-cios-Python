# Desafio 079 – Valores Únicos em uma Lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista, ele não será adicionado. No final, exiba todos os valores únicos digitados, em ordem crescente.

valores = []

# Loop para receber valores do usuário, O loop continua até que o usuário digite -1
while True:
    valor = int(input('Digite um valor (ou -1 para sair): '))
    if valor == -1:
        break
    
    # Verifica se o valor já existe na lista
    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor já existe na lista. Nâo será adicionado.')
        
valores.sort() # valores em ordem crescente
print('-' * 40)
print(f'Os valores únicos digitados foram: {valores}')
print('-' * 40)