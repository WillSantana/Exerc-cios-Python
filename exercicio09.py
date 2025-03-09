frase = 'Curso em Video Python'
print (frase) # Exibe a string inteira

print(frase[3])  # Exibe o caractere na posição 3 -> 's'

print(frase[3:13])  # Exibe os caracteres da posição 3 até a 12 (não inclui 13) -> 'so em Vide'

print(frase[:13])  # Exibe os caracteres do início até a posição 12 -> 'Curso em Vide'

print(frase[13:])  # Exibe os caracteres da posição 13 até o final -> 'o Python'

print(frase[1:15:2])  # Exibe de 1 a 14, pulando de 2 em 2 -> 'us mVd'

print(frase[2::2])  # Exibe de 2 até o final, pulando de 2 em 2 -> 'rsoe ietn'

print(frase[::2])  # Exibe toda a string, pulando de 2 em 2 -> 'Cro mVdoPto'

print(frase.upper().count('O'))  # Conta quantas vezes 'O' aparece na string em maiúsculas

print(frase.upper().find('O'))  # Encontra a posição da primeira ocorrência de 'O' na string maiúscula

print(frase.upper().rfind('O'))  # Encontra a posição da última ocorrência de 'O' na string maiúscula

print('curso' in frase.lower())  # Verifica se 'curso' está presente na string (em minúsculas)

print(frase.replace('Python', 'Android'))  # Substitui 'Python' por 'Android'

print(frase.upper())  # Transforma toda a string em maiúsculas

print(frase.lower())  # Transforma toda a string em minúsculas

print(frase.capitalize())  # Transforma apenas o primeiro caractere em maiúscula e o resto em minúsculas

print(frase.title())  # Transforma cada palavra da string com a primeira letra maiúscula

print(frase.strip())  # Remove espaços extras no início e no fim da string

print(frase.rstrip())  # Remove espaços extras apenas do lado direito da string

print(frase.lstrip())  # Remove espaços extras apenas do lado esquerdo da string

print(frase.split())  # Divide a string em uma lista de palavras

print('-'.join(frase))  # Junta as palavras da lista com o caractere especificado

print(len(frase))  # Exibe o tamanho da string

print(len (frase) - frase.count(' ')) # Exibe o tamanho da string sem contar os espaços

print(frase.find(' '))  # Encontra a posição do primeiro espaço

print(frase.rfind(' '))  # Encontra a posição do último espaço



