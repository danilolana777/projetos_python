def calculadora():

    print("Calculadora Simples")
    print("1. Soma")
    print("2, Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    try:
        opc = int(input("Escolha a operação (1-5): "))
        if opc < 1 or opc > 5:
            print("Digite um Número entre 1 e 5!")
            return False
        if opc == 5:
            print ("Programa encerrado!")
            return True
        
    except ValueError:
        print("Entrada Inválida! Digite um número.")
        return False
    
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada Inválida! Digite apenas Números.")
        return False
    
    match opc:
        case 1: 
            resultado = n1 + n2 
            print (f"Resultado: {n1} + {n2} = {resultado}")
        case 2: 
            resultado = n1 - n2 
            print (f"Resultado: {n1} - {n2} = {resultado}")
        case 3: 
            resultado = n1 * n2 
            print (f"Resultado: {n1} x {n2} = {resultado}")
        case 4: 
            if n2 == 0:
                print("Não é permitido fazer divisão por 0!")
                return False
            resultado = n1 / n2 
            print (f"Resultado: {n1} : {n2} = {resultado:.2f}")
        case _:
            print ("Operação Inválida!")
    return False

if __name__ == "__main__":
    sair = False
    while not sair:
        sair = calculadora()
