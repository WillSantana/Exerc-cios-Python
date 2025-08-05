import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
import json
import os
import csv
from tkcalendar import DateEntry
from plyer import notification
import shutil
from threading import Timer
import dropbox  # Requer instalação
import openai   # Requer instalação

class GerenciadorTarefas:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Gerenciador 3.0 ★")
        self.root.geometry("1000x700")
        
        # Configurações iniciais
        self.tarefas = []
        self.lixeira = []
        self.tema_escuro = False
        self.idioma_atual = "pt"
        self.carregar_configuracoes()
        
        # Inicializa componentes
        self.criar_widgets()
        self.aplicar_tema()
        self.carregar_tarefas()
        self.backup_automatico()
        self.verificar_lembretes()

    # ======================
    # 1. SISTEMA DE ARQUIVOS
    # ======================
    def carregar_configuracoes(self):
        if os.path.exists("config.json"):
            with open("config.json", "r") as f:
                config = json.load(f)
                self.tema_escuro = config.get("tema_escuro", False)
                self.idioma_atual = config.get("idioma", "pt")

    def salvar_configuracoes(self):
        with open("config.json", "w") as f:
            json.dump({
                "tema_escuro": self.tema_escuro,
                "idioma": self.idioma_atual
            }, f)

    def carregar_tarefas(self):
        try:
            if os.path.exists("tarefas.json"):
                with open("tarefas.json", "r") as f:
                    self.tarefas = json.load(f)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar tarefas:\n{str(e)}")

    def salvar_tarefas(self):
        try:
            with open("tarefas.json", "w") as f:
                json.dump(self.tarefas, f, indent=4)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar tarefas:\n{str(e)}")

    def backup_automatico(self):
        if not os.path.exists("backups"):
            os.makedirs("backups")
        
        backup_path = f"backups/tarefas_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        shutil.copy2("tarefas.json", backup_path)
        
        # Agenda próximo backup em 1 hora
        Timer(3600, self.backup_automatico).start()

    # =================
    # 2. INTERFACE
    # =================
    def definir_cores(self):
        return {
            "light": {
                "fundo": "#f0f0f0",
                "texto": "#333333",
                "botao": "#4CAF50",
                "lista": "#ffffff",
                "frame": "#e0e0e0",
                "destaque": "#2196F3"
            },
            "dark": {
                "fundo": "#1e1e1e",
                "texto": "#f0f0f0",
                "botao": "#1E88E5",
                "lista": "#2d2d2d",
                "frame": "#3d3d3d",
                "destaque": "#FF9800"
            }
        }["dark" if self.tema_escuro else "light"]

    def criar_widgets(self):
        self.cores = self.definir_cores()
        
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.cores["fundo"])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Barra de ferramentas
        self.criar_barra_ferramentas()
        
        # Painel de controle
        self.criar_painel_controle()
        
        # Treeview (lista de tarefas)
        self.criar_lista_tarefas()
        
        # Barra de status
        self.criar_barra_status()

    def criar_barra_ferramentas(self):
        toolbar = tk.Frame(self.main_frame, bg=self.cores["frame"])
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        # Botões da barra de ferramentas
        ttk.Button(toolbar, text="🌙/☀️", command=self.alternar_tema).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📊 Estatísticas", command=self.mostrar_estatisticas).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📤 Exportar", command=self.exportar_csv).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🗑️ Lixeira", command=self.mostrar_lixeira).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🤖 Sugerir", command=self.sugerir_tarefas).pack(side=tk.RIGHT, padx=2)

    def criar_painel_controle(self):
        panel = tk.Frame(self.main_frame, bg=self.cores["frame"])
        panel.pack(fill=tk.X, pady=(0, 10))
        
        # Entrada de tarefa
        tk.Label(panel, text="Nova Tarefa:", bg=self.cores["frame"], fg=self.cores["texto"]).grid(row=0, column=0, padx=5)
        self.entrada_tarefa = tk.Entry(panel, width=40, bg=self.cores["lista"], fg=self.cores["texto"])
        self.entrada_tarefa.grid(row=0, column=1, padx=5)
        self.entrada_tarefa.bind("<Return>", lambda e: self.adicionar_tarefa())
        
        # Prioridade
        tk.Label(panel, text="Prioridade:", bg=self.cores["frame"], fg=self.cores["texto"]).grid(row=0, column=2, padx=5)
        self.combo_prioridade = ttk.Combobox(panel, values=["⭐️ Alta", "⏳ Média", "✅ Baixa"], width=10)
        self.combo_prioridade.grid(row=0, column=3, padx=5)
        self.combo_prioridade.current(1)
        
        # Data
        tk.Label(panel, text="Data:", bg=self.cores["frame"], fg=self.cores["texto"]).grid(row=0, column=4, padx=5)
        self.calendario = DateEntry(panel, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.calendario.grid(row=0, column=5, padx=5)
        
        # Categoria
        tk.Label(panel, text="Categoria:", bg=self.cores["frame"], fg=self.cores["texto"]).grid(row=0, column=6, padx=5)
        self.combo_categoria = ttk.Combobox(panel, values=["Trabalho", "Pessoal", "Estudos"], width=10)
        self.combo_categoria.grid(row=0, column=7, padx=5)
        self.combo_categoria.current(0)
        
        # Botão Adicionar
        tk.Button(panel, text="Adicionar", command=self.adicionar_tarefa, 
                 bg=self.cores["botao"], fg="white").grid(row=0, column=8, padx=5)

    def criar_lista_tarefas(self):
        # Frame para Treeview e Scrollbar
        tree_frame = tk.Frame(self.main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("status", "tarefa", "prioridade", "categoria", "data"),
            show="headings",
            yscrollcommand=scrollbar.set,
            selectmode="extended"
        )
        
        # Configuração das colunas
        colunas = [
            ("status", "Status", 60),
            ("tarefa", "Tarefa", 300),
            ("prioridade", "Prioridade", 100),
            ("categoria", "Categoria", 100),
            ("data", "Data", 100)
        ]
        
        for col_id, heading, width in colunas:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor="center")
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Configura tags para linhas
        self.tree.tag_configure("concluido", foreground="#777777")
        self.tree.tag_configure("alta", background="#ffdddd")
        self.tree.tag_configure("media", background="#ffffcc")
        self.tree.tag_configure("baixa", background="#ddffdd")
        
        # Eventos
        self.tree.bind("<Double-1>", self.alternar_conclusao)
        self.tree.bind("<Delete>", lambda e: self.remover_tarefa())

    def criar_barra_status(self):
        status_bar = tk.Frame(self.root, bd=1, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto...")
        
        tk.Label(
            status_bar,
            textvariable=self.status_var,
            anchor=tk.W
        ).pack(fill=tk.X)

    # =====================
    # 3. FUNCIONALIDADES
    # =====================
    def adicionar_tarefa(self):
        texto = self.entrada_tarefa.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Digite uma tarefa válida!")
            return
        
        nova_tarefa = {
            "texto": texto,
            "prioridade": self.combo_prioridade.get(),
            "categoria": self.combo_categoria.get(),
            "data": self.calendario.get_date().strftime("%d/%m/%Y"),
            "concluida": False,
            "notificado": False,
            "criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        
        self.tarefas.append(nova_tarefa)
        self.entrada_tarefa.delete(0, tk.END)
        self.atualizar_lista()
        self.salvar_tarefas()
        self.status_var.set(f"Tarefa adicionada: {texto}")

    def remover_tarefa(self):
        selecionados = self.tree.selection()
        if not selecionados:
            messagebox.showwarning("Aviso", "Selecione ao menos uma tarefa!")
            return
        
        if messagebox.askyesno("Confirmar", f"Remover {len(selecionados)} tarefa(s)?"):
            # Remove em ordem reversa para manter os índices válidos
            for item in reversed(selecionados):
                indice = self.tree.index(item)
                self.lixeira.append(self.tarefas.pop(indice))
            
            self.atualizar_lista()
            self.salvar_tarefas()
            self.status_var.set(f"{len(selecionados)} tarefa(s) movida(s) para a lixeira")

    def alternar_conclusao(self, event):
        item = self.tree.focus()
        if item:
            indice = self.tree.index(item)
            self.tarefas[indice]["concluida"] = not self.tarefas[indice]["concluida"]
            self.tarefas[indice]["conclusao"] = datetime.now().strftime("%d/%m/%Y %H:%M") if self.tarefas[indice]["concluida"] else ""
            self.atualizar_lista()
            self.salvar_tarefas()

    def atualizar_lista(self):
        self.tree.delete(*self.tree.get_children())
        
        for tarefa in self.tarefas:
            status = "✔️" if tarefa["concluida"] else "❌"
            tags = ("concluido",)
            
            # Destaque por prioridade
            if "⭐️" in tarefa["prioridade"]:
                tags += ("alta",)
            elif "⏳" in tarefa["prioridade"]:
                tags += ("media",)
            else:
                tags += ("baixa",)
            
            self.tree.insert(
                "",
                tk.END,
                values=(
                    status,
                    tarefa["texto"],
                    tarefa["prioridade"],
                    tarefa["categoria"],
                    tarefa["data"]
                ),
                tags=tags
            )

    # =====================
    # 4. FUNÇÕES AVANÇADAS
    # =====================
    def mostrar_estatisticas(self):
        total = len(self.tarefas)
        concluidas = sum(1 for t in self.tarefas if t["concluida"])
        percentual = (concluidas / total * 100) if total > 0 else 0
        
        # Tarefas por categoria
        categorias = {}
        for t in self.tarefas:
            categorias[t["categoria"]] = categorias.get(t["categoria"], 0) + 1
        
        # Tarefas por prioridade
        prioridades = {"⭐️ Alta": 0, "⏳ Média": 0, "✅ Baixa": 0}
        for t in self.tarefas:
            prioridades[t["prioridade"]] += 1
        
        # Criar janela de estatísticas
        stats_win = tk.Toplevel(self.root)
        stats_win.title("Estatísticas")
        
        tk.Label(stats_win, text="📊 Estatísticas de Produtividade", font=("Arial", 14)).pack(pady=10)
        
        frame_main = tk.Frame(stats_win)
        frame_main.pack(padx=10, pady=10)
        
        # Estatísticas gerais
        frame_geral = tk.LabelFrame(frame_main, text="Geral")
        frame_geral.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        tk.Label(frame_geral, text=f"Total de Tarefas: {total}").pack(anchor="w")
        tk.Label(frame_geral, text=f"Concluídas: {concluidas} ({percentual:.1f}%)").pack(anchor="w")
        
        # Por categoria
        frame_cat = tk.LabelFrame(frame_main, text="Por Categoria")
        frame_cat.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        for cat, qtd in categorias.items():
            tk.Label(frame_cat, text=f"{cat}: {qtd}").pack(anchor="w")
        
        # Por prioridade
        frame_pri = tk.LabelFrame(frame_main, text="Por Prioridade")
        frame_pri.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        for pri, qtd in prioridades.items():
            tk.Label(frame_pri, text=f"{pri}: {qtd}").pack(anchor="w")
        
        # Gráfico simples (usando caracteres)
        frame_graph = tk.LabelFrame(frame_main, text="Progresso")
        frame_graph.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        if total > 0:
            bar_len = 20
            filled = int(bar_len * percentual / 100)
            bar = "[" + "=" * filled + " " * (bar_len - filled) + "]"
            tk.Label(frame_graph, text=bar).pack()
            tk.Label(frame_graph, text=f"{percentual:.1f}% concluído").pack()

    def exportar_csv(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Status", "Tarefa", "Prioridade", "Categoria", "Data", "Conclusão"])
                
                for tarefa in self.tarefas:
                    writer.writerow([
                        "Concluída" if tarefa["concluida"] else "Pendente",
                        tarefa["texto"],
                        tarefa["prioridade"],
                        tarefa["categoria"],
                        tarefa["data"],
                        tarefa.get("conclusao", "")
                    ])
            
            messagebox.showinfo("Sucesso", f"Tarefas exportadas para:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao exportar:\n{str(e)}")

    def mostrar_lixeira(self):
        lixeira_win = tk.Toplevel(self.root)
        lixeira_win.title("Lixeira")
        lixeira_win.geometry("600x400")
        
        tk.Label(lixeira_win, text="🗑️ Tarefas Excluídas", font=("Arial", 14)).pack(pady=10)
        
        tree = ttk.Treeview(lixeira_win, columns=("tarefa", "prioridade", "data_exclusao"), show="headings")
        tree.heading("tarefa", text="Tarefa")
        tree.heading("prioridade", text="Prioridade")
        tree.heading("data_exclusao", text="Excluída em")
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for item in self.lixeira:
            tree.insert("", tk.END, values=(
                item["texto"],
                item["prioridade"],
                datetime.now().strftime("%d/%m/%Y %H:%M")
            ))
        
        frame_botoes = tk.Frame(lixeira_win)
        frame_botoes.pack(pady=10)
        
        tk.Button(frame_botoes, text="Restaurar Selecionada", command=lambda: self.restaurar_tarefa(tree)).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Esvaziar Lixeira", command=lambda: self.esvaziar_lixeira(lixeira_win)).pack(side=tk.LEFT, padx=5)

    def restaurar_tarefa(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para restaurar!")
            return
        
        indice = tree.index(selecionado[0])
        self.tarefas.append(self.lixeira.pop(indice))
        self.atualizar_lista()
        self.salvar_tarefas()
        tree.delete(selecionado[0])
        self.status_var.set("Tarefa restaurada com sucesso!")

    def esvaziar_lixeira(self, janela):
        if messagebox.askyesno("Confirmar", "Esvaziar permanentemente a lixeira?"):
            self.lixeira.clear()
            janela.destroy()
            self.status_var.set("Lixeira esvaziada!")

    def sugerir_tarefas(self):
        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "user", 
                    "content": "Sugira 3 tarefas produtivas para fazer hoje, formatadas como: 'Descrição da tarefa|Prioridade (Alta/Média/Baixa)|Categoria (Trabalho/Pessoal/Estudos)'"
                }]
            )
            
            sugestoes = resposta.choices[0].message.content.split("\n")
            
            for sug in sugestoes[:3]:  # Pega até 3 sugestões
                if "|" in sug:
                    desc, pri, cat = sug.split("|")
                    self.tarefas.append({
                        "texto": desc.strip(),
                        "prioridade": f"⭐️ {pri.split('(')[0].strip()}",
                        "categoria": cat.split("(")[0].strip(),
                        "data": datetime.now().strftime("%d/%m/%Y"),
                        "concluida": False,
                        "notificado": False,
                        "criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
                    })
            
            self.atualizar_lista()
            self.salvar_tarefas()
            self.status_var.set("Tarefas sugeridas adicionadas!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao obter sugestões:\n{str(e)}")

    def verificar_lembretes(self):
        agora = datetime.now()
        hoje = agora.strftime("%d/%m/%Y")
        
        for tarefa in self.tarefas:
            if not tarefa["notificado"] and tarefa["data"] == hoje:
                # Verifica se está dentro de 1 hora do horário atual
                try:
                    hora_tarefa = datetime.strptime(tarefa["data"] + " 12:00", "%d/%m/%Y %H:%M")  # Assume meio-dia
                    if abs((agora - hora_tarefa).total_seconds()) <= 3600:
                        notification.notify(
                            title=f"📅 Lembrete: {tarefa['texto']}",
                            message=f"Prioridade: {tarefa['prioridade']}\nCategoria: {tarefa['categoria']}",
                            timeout=10
                        )
                        tarefa["notificado"] = True
                except:
                    pass
        
        # Verifica novamente em 5 minutos
        self.root.after(300000, self.verificar_lembretes)

    def alternar_tema(self):
        self.tema_escuro = not self.tema_escuro
        self.cores = self.definir_cores()
        self.aplicar_tema()
        self.salvar_configuracoes()

    def aplicar_tema(self):
        # Aplica cores a todos os widgets
        self.root.config(bg=self.cores["fundo"])
        
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.config(bg=self.cores["frame"])
            
            if isinstance(widget, tk.Label):
                widget.config(bg=self.cores["frame"], fg=self.cores["texto"])
        
        # Atualiza Treeview
        style = ttk.Style()
        style.theme_use("default")
        
        style.configure(
            "Treeview",
            background=self.cores["lista"],
            foreground=self.cores["texto"],
            fieldbackground=self.cores["lista"]
        )
        
        style.map(
            "Treeview",
            background=[("selected", self.cores["destaque"])],
            foreground=[("selected", "white")]
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefas(root)
    root.mainloop()