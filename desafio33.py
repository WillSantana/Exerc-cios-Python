n1 = int(input('Digite um primeiro numero: '))
n2 = int(input('Digite um segundo numero: '))
n3 = int(input('Digite um terceiro numero: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

menor = n1
if n2 < n1 and n2 < n3: # n2 é o menor
    menor = n2
if n3 < n1 and n3 < n2: # n3 é o menor
    menor = n3
    

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')