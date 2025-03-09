nome = str(input('Digite um nome: ')).strip()
print(nome)
print('Silva' in nome) # Verifica se a palavra 'Silva' está contida no nome digitado.
print('O nome tem:',nome.count(' '), 'espaços em branco') # Conta quantos espaços em branco tem no nome.
print(nome.find(' ')) # Encontra a primeira ocorrência de um espaço em branco.
print(nome.rfind(' ')) # Encontra a última ocorrência de um espaço em branco.
print(nome.split()) # Divide o nome em uma lista de palavras.
print(nome.split()[0]) # Exibe a primeira palavra do nome.
