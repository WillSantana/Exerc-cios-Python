# Desafio 080 – Lista Ordenada sem Repetições
# Crie um programa que leia 5 números e os insira em uma lista de forma que a lista permaneça 
# ordenada sem usar o método sort().

numeros = []
# Loop para receber 5 valores do usuário, O loop continua até que o usuário digite 5 valores
for i in range(5):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if i == 0 or valor > numeros[-1]:
        numeros.append(valor)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
    print(f'Lista atual: {numeros}')

print(f'Os valores digitados em ordem foram: {numeros}')
print('-' * 40)
print(f'Os valores digitados foram: {numeros}')
print('-' * 40)