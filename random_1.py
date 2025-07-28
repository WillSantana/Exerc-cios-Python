import random

# Gera números aleatórios

valor = random.randint(1, 21)
print(valor)

#-------------------------------------------

print("Gerar cinco números aleatórios entre 1 e 50: \n ")
for i in range(5):
    n = random.randint(1, 50)
    print(f'Número {i+1}: {n}')
    
#-------------------------------------------

# Numeros aleatórios de ponto flutuante utilizando a função random.

valor = random.random()
print(f"Número gerado: {round(valor * 10,2)}")

#--------------------------------------------

# Números aleatórios de ponto flutuante utilizando a função uniform.

valor = random.uniform(1, 30)
print(f"Número gerado: {round(valor, 4)}")


#---------------------------------------------

# Sorteia um número aleatório apartir de uma lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteio = random.choice(lista)
print(f"Número sorteado: {sorteio}")

#-----------------------------------------------

# sortear varios números apartir de um lista.

lista = [2, 4, 6, 9, 10, 13, 15, 18, 20, 21, 27, 30]
sorteio = random.sample(lista, 3)
print(f"Número sorteado: {sorteio}")

#-------------------------------------------------

# Embaralhar aleatóriamente um numero apartir de um lista.

lista = [2, 4, 6, 9, 10, 13, 15, 18, 20, 21, 27, 30]
print(f"Lista original: {lista}")
print(f"Embaralhar a lista:")
n = random.shuffle(lista)
print(f"Lista embaralhada: {lista}")


