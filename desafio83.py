# Desafio 083 – Validando Expressões Matemáticas
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
# abertos e fechados na ordem correta.

expressao = str(input('Digite uma expressão: '))
pilha = []  
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')
print('-' * 40)
print('Fim do programa.')
print('-' * 40)

