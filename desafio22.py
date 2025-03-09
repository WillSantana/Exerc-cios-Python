nome = str(input('Digite o seu Nome Completo: ')).strip()
print(nome)
print('Seu nome todo em Maiusculo:', nome.upper()) # Transforma o nome em maiusculo.
print('Seu nome todo em Minusculo:', nome.lower()) # Transforma o nome em minusculo.
print('Tem um total de:', len(nome) - nome.count(' ')) # Conta o total de letras do nome.
print('O primeiro nome tem: ', nome.find(' ')) # Encontra a primeira ocorrência de um espaço em branco.
separa = nome.split()
print('O primeiro nome é: ' + separa[0] + ' e ele tem ' + str(len(separa[0])) + ' letras.') # Exibe a primeira palavra do nome e o total de letras.
