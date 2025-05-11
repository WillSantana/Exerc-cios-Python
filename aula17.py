# Estrutura de lista
minha_lista = [1, 2, 3, 4, 5]

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Adicionar itens na lista
minha_lista.append(6)  # Adiciona um item ao final
minha_lista.extend([7, 8])  # Adiciona vários itens ao final
minha_lista.sort(reverse=True)  # Ordena a lista em ordem decrescente
minha_lista.insert(0, 0)  # Adiciona um item no início

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Remover itens da lista
minha_lista.remove(3)  # Remove o primeiro item com valor 3
if 5 in minha_lista:
    minha_lista.remove(5)  # Remove o primeiro item com valor 5
else:
    print("O valor 5 não está na lista.")
removido = minha_lista.pop()  # Remove e retorna o último item

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Exibir a lista preenchida
valores = []
valores.append(10)  # Adiciona o valor 10 à lista
valores.append(20)  # Adiciona o valor 20 à lista
valores.append(30)  # Adiciona o valor 30 à lista

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Exibir a lista preenchida com valores digitados pelo usuário
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

a = [1, 2, 3]
b = a[:]  # Copia a lista a para b
b[2] = 4  # Altera o valor na posição 2 de b
print(f'Lista A: {a}')  # Exibe a lista a
print(f'Lista B: {b}')  # Exibe a lista b

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Estrutura de tupla
minha_tupla = (10, 20, 30, 40, 50)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Adicionar itens na tupla (criando uma nova tupla)
minha_tupla = minha_tupla + (60,)  # Adiciona um item ao final
minha_tupla = (5,) + minha_tupla  # Adiciona um item no início
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Remover itens da tupla (criando uma nova tupla)
minha_tupla = tuple(x for x in minha_tupla if x != 30)  # Remove o item com valor 30