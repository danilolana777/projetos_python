#abre a lista principal
lista_de_tarefas = []

def inicializar_funcao():
    ver_tarefas()
    if not lista_de_tarefas:
        print("Nenhuma Tarefa Registrada!")
    return
#Função que pede a tarefa e adiciona ela a lista principal
def adicionar_tarefa():
    tarefa = input("\nDigite a tarefa:")
    if not tarefa.isalpha():
        lista_de_tarefas.append(tarefa)
        print(f"\n\033[32mTarefa Adicionada com Sucesso!\033[0m")
        return menu
    else:
        print("\n\033[31mDigite uma tarefa Válida!\033[0m")

#Função que verifica se existe alguma tarefa na lista principal e depois as exibe com seu índice + 1
def ver_tarefas():
    if not lista_de_tarefas:
        print("\n\033[31mNenhuma Tarefa Registrada! \033[0m")
        return menu()
        
      
    else:
        print("\n-----Tarefas-Registradas-----")
        for i,t in enumerate(lista_de_tarefas, start = 1):
            print (f"{i}. {t}")

def alterar_tarefa():
    inicializar_funcao()
    try:
        numero_altera_tarefa = int(input("Digite o número da tarefa que deseja alterar: "))
        nova_tarefa = input("\nDigite a alteração: ")
        lista_de_tarefas[numero_altera_tarefa - 1] = nova_tarefa
        print (f"\n\033[32mA tarefa {numero_altera_tarefa} foi Alterada com sucesso!\033[0m")
    except ValueError:
        print("Escreve direito animal")
#Função que remove uma tarefa especifica da lista por meio do .pop
def concluir_tarefa():
    ver_tarefas()
    if ver_tarefas:
        try:
            numero_tarefa = int(input("Digite o número da Tarefa que deseja concluir: "))
            #verifica se existe uma tarefa do numero digitado
            if 1 <= numero_tarefa <= len(lista_de_tarefas):
                remover = lista_de_tarefas.pop(numero_tarefa - 1)
                print (f"\n\033[32mA Tarefa {numero_tarefa} foi concluida com Sucesso!\033[0m")
            else:
                print("\n\033[31m-----Digite um número Válido!-----\033[0m")
                return concluir_tarefa()
        except ValueError:
            print("\n\033[31mDigite um número Válido!\033[0m")


#função que apaga todas as tarefas

def clear():
    ver_tarefas()
    lista_de_tarefas.clear()
    print("\n\033[32mTodas as Tarefas foram apagadas!\033[0m")

#Função que exibe o menu, faz a verificação da opção escolhida e chama a função do caso

def menu():
    print("\n", 10*" =", "\n   Lista de Tarefas:", "\n", 10*" =")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir Tarefa")
    print("4. Limpar Todas as Tarefas")
    print("5. Alterar Tarefa")
    print("6. Sair")
    try:
        opc = int(input("\nDigite uma das operações (1-6): "))
        if opc < 1 or opc > 6:
            print("\n\033[31m---Digite um Número entre 1 a 6!---\033[0m")
            return False
        if opc == 6:
            print ("\n\033[33m---Progama encerrado!---\033[0m")
            return True
    except ValueError:
            print("\n\033[31mEntrada Inválida! Digite um número.\033[0m")
            return False
    match opc:
        case 1:
            adicionar_tarefa()
        case 2:
            ver_tarefas()
        case 3:
            concluir_tarefa()
        case 4:
            clear()
        case 5:
            alterar_tarefa()
        case _:
            print("\n\033[31m---Operação invalida!---\033[0m")
#Chama o código todo
if __name__ == "__main__":
    sair = False 
    while not sair:
        sair = menu()


 
