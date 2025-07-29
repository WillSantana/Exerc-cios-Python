# # Exemplo 1: Função sem parâmetros
# def saudacao():
#     print("Olá, seja bem-vindo!")
# saudacao()


# # Exemplo 2: Função com parâmetro obrigatório

# def dobrar(numero):
#     return numero * 2


# # Exemplo 3: Função com parâmetro opcional
# def apresentar(nome, idade=18):
#     print(f"Nome: {nome}, Idade: {idade}")
# apresentar("João")  # Usa o valor padrão de idade

# # Exemplo 4: Função com vários parâmetros
# def soma(a, b, c):
#     return a + b + c

# # Exemplo 5: Função que retorna múltiplos valores
# def operacoes(x, y):
#     soma = x + y
#     produto = x * y
#     return soma, produto

# # Exemplo 6: Função com argumentos nomeados
# def mostrar_info(nome, cidade):
#     print(f"{nome} mora em {cidade}")

# # Exemplo 7: Função com número variável de argumentos
# def listar_nomes(*nomes):
#     for nome in nomes:
#         print(nome)

# # Exemplo 8: Função com parâmetros opcionais e obrigatórios
# def cadastro(nome, email=None, telefone=None):
#     print(f"Nome: {nome}")
#     if email:
#         print(f"Email: {email}")
#     if telefone:
#         print(f"Telefone: {telefone}")

# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Exemplo 2: Função com parâmetro obrigatório, aprimorado

# def dobrar(numero):
#     return numero * 2
# entrada_do_usuario = input("Digite um numero: ")
# try:
#     # Tenta converter a entrada para um numero inteiro.
#     numero_convertido = int(entrada_do_usuario)
#     # chama a função dobrar com o numero convertido.
#     resultado = dobrar(numero_convertido)
#     # imprimir o resultado.
#     print(f"O dobro de  {numero_convertido} é {resultado}")
# except ValueError:
#     # Se a conversão falhar, (ex: usuario digitou 'abc'), captura o erro.
#     print("Entrada inválida. Por favor, digite um número inteiro.")
# except Exception as e:
#     # Captura qualquer outro erro inesperado.
#     print(f"Ocorreu um erro inesperado: {e}")
    
#  Exemplo 3: Função com parâmetro opcional 

def apresentar(nome, idade= 38):
    print(f"Meu Nome é: {nome}, e tenho {idade} anos.")
try:
    entrada_nome = input("Digite seu nome: ")
    entrada_idade = int(input("Digite sua idade: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um nome e uma idade valida.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
apresentar(entrada_nome, entrada_idade)

def apresentar(nome, idade)
    print(f"Nome")