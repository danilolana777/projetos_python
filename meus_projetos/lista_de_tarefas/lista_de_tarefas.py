#abre a lista principal
lista_de_tarefas = []
lixeira_de_tarefas = []
def inicializar_funcao():
    ver_tarefas()
    if not lista_de_tarefas:
        print("\n\033[31mNenhuma Tarefa Registrada!\033[0m")
    return
#Função que pede a tarefa e adiciona ela a lista principal
def adicionar_tarefa():
    tarefa = input("\nDigite a tarefa:").strip()
    if tarefa and not tarefa.isdigit() and not tarefa.isspace():
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
    print("\n-----Tarefas-Registradas-----")
    for i,t in enumerate(lista_de_tarefas, start = 1):
        print (f"{i}. {t}")

def lixeira():
    if not lixeira_de_tarefas:
        print("\n\033[31m Nenhuma Tarefa na lixeira!\033[0m")
        return menu()
    print("\n----LIXEIRA----")
    for i, t in enumerate(lixeira_de_tarefas, start = 1):
        print (f"{i}. {t}")

def alterar_tarefa():
    inicializar_funcao()
    try:
        numero_altera_tarefa = int(input("Digite o número da tarefa que deseja alterar: "))
        if numero_altera_tarefa <= 1 or numero_altera_tarefa <= len(lista_de_tarefas):
            nova_tarefa = input("\nDigite a alteração: ")
            if nova_tarefa and not nova_tarefa.isdigit() and not nova_tarefa.isspace():
                lista_de_tarefas[numero_altera_tarefa - 1] = nova_tarefa
                print (f"\n\033[32mA tarefa {numero_altera_tarefa} foi Alterada com sucesso!\033[0m")
            else:
                print("\n\033[31mDigite uma tarefa Válida!\033[0m")
        else:
            print("\n\033[31m-----Digite um número Válido!-----\033[0m")
            return alterar_tarefa
    except ValueError:
        print("\n\033[31mEscreve direito animal\033[0m")
#Função que remove uma tarefa especifica da lista por meio do .pop
def concluir_tarefa():
    ver_tarefas()
    if lista_de_tarefas:
        try:
            numero_tarefa = int(input("Digite o número da Tarefa que deseja concluir: "))
            #verifica se existe uma tarefa do numero digitado
            if 1 <= numero_tarefa <= len(lista_de_tarefas):
                remover = lista_de_tarefas.pop(numero_tarefa - 1)
                lixeira_de_tarefas.append(remover)
                print (f"\n\033[32mA Tarefa {numero_tarefa} foi concluida com Sucesso!\033[0m")
            else:
                print("\n\033[31m-----Digite um número Válido!-----\033[0m")
                return concluir_tarefa()
        except ValueError:
            print("\n\033[31mDigite um número Válido!\033[0m")
            
    
#função que apaga todas as tarefas

def clear():
    ver_tarefas()
    lixeira_de_tarefas.extend(lista_de_tarefas)#utiliza o extend para passar cada elemento da lista individualmente, para não formar uma matriz!
    lista_de_tarefas.clear()
    print("\n\033[32mTodas as Tarefas foram Concluídas!!\033[0m")

def lixeira_clear():
    if lixeira_de_tarefas:
        lixeira_de_tarefas.clear()
        print("\n\033[32mA lixeira foi Esvaziada!\033[0m")
    else:
        print("\n\033[31mNão há nenhum item na Lixeira!\033[0m")
#Função que exibe o menu, faz a verificação da opção escolhida e chama a função do caso

def menu():
    print("\n", 10*" =", "\n   Lista de Tarefas:", "\n", 10*" =")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir Tarefa")
    print("4. Concluir Todas as Tarefas")
    print("5. Alterar Tarefa")
    print("6. Lixeira")
    print("7. Esvaziar Lixeira")
    print("8. Sair")
    try:
        opc = int(input("\nDigite uma das operações (1-8): "))
        if opc < 1 or opc > 8:
            print("\n\033[31m---Digite um Número entre 1 a 8!---\033[0m")
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
            case 6:
                lixeira()
            case 7:
                lixeira_clear()
            case 8:
                print ("\n\033[33m---Progama encerrado!---\033[0m")
                return True
            case _:
                print("\n\033[31m---Operação invalida!---\033[0m")
    except ValueError:
            print("\n\033[31mEntrada Inválida! Digite um número.\033[0m")
        
#Chama o código todo
if __name__ == "__main__":
    sair = False 
    while not sair:
        sair = menu()


 
