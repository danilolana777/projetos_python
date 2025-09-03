lista_de_tarefas = []
tarefas_concluidas = []

erro_operacao = ("\n\033[31mOperação Inválida, Digite um Número de 0 a 6!\033[0m")
erro_operacao_reset = ("\n\033[31mOperação Inválida, (s), para sim e (n), para não!\033[0m")
erro_tarefa = ("\n\033[31mDigite Uma Tarefa Válida!\033[0m")
erro_numtarefa = ("\n\033[31mNúmero da Tarefa Inválido!\033[0m")
erro_notarefa = ("\n\033[31mNenhuma Tarefa Registrada!\033[0m")
erro_notarefa_concluida = ("\n\033[31mNenhuma Tarefa foi Concluída!\033[0m")
erro_notreset = ("\n\033[31mNão a nada para Resetar!\033[0m")
erro_reset = ("\n\033[31mO progama Não foi Resetado!\033[0m")
true_addtarefa = ("\n\033[32mTarefa Adicionada com Sucesso!\033[0m")
true_altertarefa = ("\n\033[32mTarefa Alterada com Sucesso!\033[0m")
true_deltarefa = ("\n\033[32mTarefa Concluída com Sucesso!\033[0m")
true_reset = ("\n\033[32mProgama resetado com SUCESSO!\033[0m")
exit = ("\n\033[33m-----Programa-Encerrado-----\033[0m")

def inserir_tarefa():
    tarefa = input("Digite a Tarefa que deseja adicionar: ").strip()
    if tarefa and not tarefa.isdigit() and not tarefa.isspace():
        lista_de_tarefas.append(tarefa)
        print (true_addtarefa)
        return
    else:
        print (erro_tarefa)
        return

def ver_tarefas():
    if lista_de_tarefas:
        print ("\n", 15*"=", "\nLista de tarefas:\n", 15*"=",)
        for i, j in enumerate(lista_de_tarefas, start= 1):
            print (f"\n{i}. {j}")
    else:
        print (erro_notarefa)
        return

def del_tarefa():
    if lista_de_tarefas:
        ver_tarefas()
        try:
            opc = int(input("Digite o número da tarefa que deseja Concluir: ")) 
            if opc >= 1 and opc <= len(lista_de_tarefas):
                remover = lista_de_tarefas.pop(opc - 1)
                tarefas_concluidas.append(remover)
                print (true_deltarefa)
                return
            else:
                print(erro_numtarefa)
                return
        except ValueError:
            print (erro_numtarefa)
            return
    else:
        print (erro_notarefa)
        return

def alter_tarefas():
    if lista_de_tarefas:
        ver_tarefas()
        try:
            opc = int(input("Digite o número da tarefa que deseja alterar: "))
            if opc >= 1 and opc <= len(lista_de_tarefas):
                nova_tarefa = input("\nDigite a alteração: ").strip()
                if nova_tarefa and not nova_tarefa.isdigit() and not nova_tarefa.isspace():
                    lista_de_tarefas[opc - 1] = nova_tarefa
                    print (true_altertarefa)
                    return
                else:
                    print (erro_tarefa)
                    return
            else:
                print (erro_numtarefa)
                return
        except ValueError:
            print (erro_numtarefa)
    else:
        print(erro_notarefa)
        return
    
def t_concluidas():
    print ("\n", 15*"=", "\nTarefas Concluídas:\n", 15*"=",)
    if tarefas_concluidas:
        for i, j in enumerate(tarefas_concluidas, start= 1):
            print (f"{i}. {j}")
        return
    else:
        print (erro_notarefa_concluida)
        return

def reset():
    if not lista_de_tarefas and not tarefas_concluidas:
        print(erro_notreset)
        return
    else:
        opc = input("\nTem certeza que deseja resetar o progama?\n\033[31misso apagará todas as tarefas pendendes e as concluídas!\033[0m\nDigite (s), para sim e (n), para não: ").strip()
        
        if opc.lower() == "s":
            lista_de_tarefas.clear()
            tarefas_concluidas.clear()
            print (true_reset)
            return
        elif opc.lower() == "n":
            print(erro_reset)
            return
        else:
            print (erro_operacao_reset)
            return
            
def menu():
    print ("\n", 15*"=", "\nLista de tarefas\n", 15*"=",)
    print ("0. Sair")
    print ("1. Inserir Tarefa")
    print ("2. Ver Tarefas")
    print ("3. Concluir tarefas")
    print ("4. Alterar tarefas")
    print ("5. Tarefas Concluidas")
    print ("6. Reset")
    try:
        global opcmain
        opcmain = int(input("Digite o número da operação: "))
        if opcmain >= 0 and opcmain <= 6:
            return main()
        else:
            print(erro_operacao)
            return
    except ValueError:
        print (erro_operacao)

def main():
    match opcmain:
        case 0:
            print (exit)
            return True
        case 1:
            inserir_tarefa()
        case 2:
            ver_tarefas()
        case 3:
            del_tarefa()
        case 4:
            alter_tarefas()
        case 5:
            t_concluidas()
        case 6:
            reset()
if __name__ == "__main__":
    sair = False 
    while not sair:
        sair = menu()
    
        