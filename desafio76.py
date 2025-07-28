# Desafio 076 – Lista de Preços com Tupla

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # Centraliza o título
print('-' * 40)

# percorre a tupla de 2 em 2
for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i + 1]
    print(f'{produto:.<30} R$ {preco:>7.2f}')
print('-' * 40)
print('FIM')
