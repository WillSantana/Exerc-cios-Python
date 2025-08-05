import tkinter as tk  # Importa a biblioteca de interface gráfica

# 1. Cria a janela principal
janela = tk.Tk()  # Cria a janela
janela.title("Interface Gráfica com Tkinter")  # Título da janela
janela.geometry("300x200")  # Tamanho (largura x altura)

# 2. Função que será chamada pelo botão
def saudacao():
    nome = entrada_nome.get()  # Pega o texto digitado
    mensagem = f"Olá, {nome}!" if nome else "Olá, usuário!"  # Condicional simplificado
    label_mensagem.config(text=mensagem)  # Atualiza o texto na tela

# 3. Elementos da interface:
# - Label (texto estático)
label_nome = tk.Label(janela, text="Digite seu nome:")
label_nome.pack(pady=10)  # `pack()` organiza o elemento na janela

# - Campo de entrada de texto
entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

# - Botão
botao_saudacao = tk.Button(janela, text="Saudar", command=saudacao)
botao_saudacao.pack(pady=10)

# - Label para exibir a mensagem
label_mensagem = tk.Label(janela, text="")
label_mensagem.pack(pady=10)

# 4. Mantém a janela aberta
janela.mainloop()

print("Interface gráfica criada com sucesso!")