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

# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#  Exemplo 3: Função com parâmetro opcional

# def apresentar(nome, idade= 38):
#     print(f"Meu Nome é: {nome}, e tenho {idade} anos.")
# while True:
#     try:
#         # Pede o nome (sempre é uma string, não precisa de conversão)
#         entrada_nome = input("Digite seu nome: ")

#         # Pede a idade e tenta converter para um número inteiro
#         entrada_idade_str = input("Digite sua idade: ") # Pega como texto primeiro
#         entrada_idade = int(entrada_idade_str) # Tenta converter para número

#         apresentar(entrada_nome, entrada_idade)

#         break
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um nome e uma idade valida.")
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado: {e}")
#         break

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# # Exemplo 4: Função com vários parâmetros
# Gerador de Ficha de Personagem


# def soma(a, b, c):
#     return a + b + c
def criar_ficha_personagem(nome, classe, nivel, arma="Nenhuma", habilidade=None):
    # parametros obrigatórios: (str)nome, (str)classe, (int) nivel.
    # ex. de classe: "Guerreiro", "Mago", "Arqueiro"
    # Arma (str, opcional): "Espada", "Arco", "Varinha", equipada pelo personagem. padrao "Nenhuma")
    # Habilidade (lista, opcional): lista de habilidades do personagem. padrao lista vazia.
    if habilidade is None:
        habilidade = []
    print("---FICHA DE PERSONAGEM---")
    print(f"Nome: {nome}")
    print(f"Classe: {classe}")
    print(f"Nível: {nivel}")
    print(f"Arma: {arma}")
    
    # verifica se o personagem tem habilidades para exibir.
    if habilidade:
        print("Habilidades:")
        for habilidade in habilidade:
            print(f" - {habilidade}")
    else:
        print("Nenhuma habilidade registrada.")
    print("------------------------------------------------------------------------------------------")
    print("\n") # quebra de linha

# -- Exemplo de como chamar a função com diferentes parâmetros
print("Chamada 1 : apenas obrigatórios")
criar_ficha_personagem("Arthas", "Guerreiro", 10)

print("-----------------------------------------------------------------------------------------------")

print("Chamada 2 : Obrigatórios + Arma")
criar_ficha_personagem("Jaina", "Mago", 12, arma="Cajado", habilidade=["Magia de Gelo", "Teleporte"])

print("-----------------------------------------------------------------------------------------------")

print("Chamada 3: Obrigatórios + Habilidades (por posição)")
criar_ficha_personagem("Sylvanas", "Arqueira", 15, "Arca Élfico", ["Tiro Preciso", "Visão Noturna"])

print("-----------------------------------------------------------------------------------------------")

print("chamada 4: Obrigatórios + Habilidades (por nome)")
criar_ficha_personagem("Thrall", "Anão", 6, habilidade=["Resistêcia", "Machado Duplo"])

print("-----------------------------------------------------------------------------------------------")

print("Chamand 5: Todos os parâmentros")
criar_ficha_personagem("frodo", "Hobbit", 5, "Faca", habilidade=["Furtividade", "Resistência à Magia"])

print("-----------------------------------------------------------------------------------------------")

print("Chamada 6: Usando padrões para arma e habilidades")
criar_ficha_personagem("Boromir", "Cavaleiro", 10) # Arma e Habilidades usarão os valores padrão

print("-----------------------------------------------------------------------------------------------")

print("Chamada 7: Todos os parâmetros por nome")
criar_ficha_personagem(nome="Gandalf", classe="Mago", nivel=15, arma="Cajado Mágico", habilidade=["Feitiços", "Sabedoria Antiga"])
