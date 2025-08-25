def list():

    lista = []
    print ("Escolha Valores para Adiconar a Lista")
    print ("1.Número inteiro")
    print ("2.Número Quebrado")
    print ("3.Texto")
    print ("4.Limpar Lista")
    print ("5.Sair do progama!") 
    try:
        opc = int(input("Digite uma opção entre 1 a 5: "))
        if opc < 1 or opc > 5:
            print ("Escolha uma opção entre 1 e 5!")
            return False
        if opc == 5:
            print ("Progama Encerrado!")
            return True
        if opc == 4:
            print ("Progama Encerrado!")
            return False
    except ValueError:
        print("Entrada Inválida! Digite um número.")
        return False
        
        
    match opc:
        case 1:
            valor = int(input("Digite um Número Inteiro: "))
        case 2:
            valor = float(input("Digite um Número Quebrado: "))
        case 3:
            valor = str(input("Digite um Texto: "))
        case _:
            print("Operação Inválida!")
    lista.append(valor)
    print (lista)




if __name__ == "__main__":
    sair = False
    while not sair:
        sair = list()


