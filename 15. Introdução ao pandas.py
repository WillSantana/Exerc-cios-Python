import pandas as pd

# df_alunos = pd.DataFrame({
#     'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
#     'nota1': [8.5, 7.0, 9.0, 6.5],
#     'nota2': [9.0, 8.0, 7.5, 8.5]
# })
# df_alunos.to_csv('alunos.csv', index=False)

# df_alunos_loaded = pd.read_csv('alunos.csv')
# print(df_alunos_loaded.head())


tarefas = [
    {'descricao': 'Estudar Python', 'concluida': False},
    {'descricao': 'Fazer compras', 'conccluida': False},
    {'descricao': 'Pagar contas', 'concluida': True}      
]

def exibir_menu():
    print("\n---Gerenciador de Tarefas---")
    print("1. Adicionar nova Tarefa")
    print("2. Ver todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair Programa")
    print("----------------------------")
    
    
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({'descricao': descricao, 'concluida': False})
    print(f"Tarefa '{descricao}' adicionada com sucesso!")
    
def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
        
print("\n---Lista de Tarefas---")
for i, tarefa in enumerate(tarefas, start=1):
    status = "✅" if tarefa.get("concluida", False) else "⏳"
    print(f"{i}. {status} {tarefa['descricao']}") # Mostra o número, status e descrição
    print("--------------------")


def marcar_tarefa_concluida():
    ver_tarefas()
    if not tarefas:
        return
    
    while True:
        try:
            num_tarefa_str = input("Digite o número da tarefa concluída: ")
            if num_tarefa_str.lower() == 'sair':
                print("Saindo do programa...")
                return
            num_tarefa_str = int(num_tarefa_str)
            indice_tarefa = num_tarefa_str - 1
            
            if 0 <= indice_tarefa < len(tarefas):
                tarefas[indice_tarefa]['concluida'] = True
                print(f"Tarefa '{tarefas[indice_tarefa]['descricao']}' marcada como concluída!")
                break
            else:
                print("Número de tarefa inválido. Por favor, digite um número da lista.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'cancelar'.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            break # Sai do loop em caso de erro grave
        
        
        def iniciar_gerenciador():
            
            while True:
                exibir_menu()
                opcao = input("Escolha uma opção: ")
                
                if opcao == '1':
                    adicionar_tarefa()
                elif opcao == '2':
                    ver_tarefas()
                elif opcao == '3':
                    marcar_tarefa_concluida()
                elif opcao == '4':
                    print("Saindo do Gerenciador de Tarefas. Até mais!")
                    break
                else:
                    print("Opção inválida. Por favor, escolha um número de 1 a 4.")

#chama a função para iniciar o gerenciador de tarefas                    
    iniciar_gerenciador()