# Lista simples em Python:
# Uma lista simples armazena elementos de forma sequencial, podendo ser de qualquer tipo.
# Exemplo:
frutas = ['maçã', 'banana', 'laranja']
print("Lista simples:", frutas)

# Lista composta em Python:
# Uma lista composta é uma lista que contém outras listas como elementos.
# Isso permite criar estruturas como tabelas (matrizes).
# Exemplo:
alunos = [
    ['Ana', 8.5],
    ['Bruno', 7.0],
    ['Carla', 9.2]
]
print("Lista composta:", alunos)

# Explicação:
# - Lista simples: cada elemento é um dado (ex: string, número).
# - Lista composta: cada elemento é uma lista, permitindo armazenar múltiplos dados relacionados.
# Exemplo usando laço for para preencher uma lista com números pares de 0 a 10
pares = []
for i in range(11):
    if i % 2 == 0:
        pares.append(i)
print("Números pares de 0 a 10:", pares)

# Exemplo usando while para criar uma lista de frutas digitadas pelo usuário (simulado)
frutas_usuario = []
contador = 0
nomes = ['uva', 'pera', 'melancia']  # Simulação de entradas do usuário
while contador < len(nomes):
    fruta = nomes[contador]
    if fruta not in frutas_usuario:
        frutas_usuario.append(fruta)
    else:
        print(f"{fruta} já está na lista.")
    contador += 1
print("Frutas digitadas:", frutas_usuario)

# Exemplo de lista composta com if/else para classificar alunos aprovados e reprovados
alunos_notas = [
    ['Lucas', 6.5],
    ['Maria', 8.0],
    ['Pedro', 4.5]
]
aprovados = []
reprovados = []
for aluno in alunos_notas:
    if aluno[1] >= 7.0:
        aprovados.append(aluno[0])
    else:
        reprovados.append(aluno[0])
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)


galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

# Exemplo de lista composta com if/else para classificar alunos aprovados e reprovados
alunos_notas = [
    ['Lucas', 6.5],
    ['Maria', 8.0],
    ['Pedro', 4.5]
]
aprovados = []
reprovados = []
for aluno in alunos_notas:
    if aluno[1] >= 7.0:
        aprovados.append(aluno[0])
    else:
        reprovados.append(aluno[0])
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)

# Exemplo de lista composta com for para calcular a média de idades
galera = list()
dados = list()
totmaior = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
    
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmaior += 1
print(f'Temos {totmaior} pessoas maiores de idade.')
# Exemplo de lista composta com if/else para classificar alunos aprovados e reprovado

