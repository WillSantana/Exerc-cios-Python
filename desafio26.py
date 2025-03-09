frase = str(input('Digite uma frase: ')).upper().strip()
print(frase)
print('A letra A aparece',frase.count('A'), 'vezes na frase') # Conta quantas vezes a letra 'a' aparece na frase.
print('A primeira letra A apareceu na posição ',frase.find('A')+1) # Encontra a primeira ocorrência da letra 'a'.
print('A última letra A apareceu na posição ',frase.rfind('A')+1) # Encontra a última ocorrência da letra 'a'

