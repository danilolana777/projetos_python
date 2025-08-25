def criar_matriz(tamanho):
    matriz = []
    print ("Digite os valores para a matriz 3x3!")
    for i in range (tamanho):
        linha = []
        for j in range (tamanho):
            valor = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def multiplicar_por_escalar(matriz, escalar, tamanho):
    resultado = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(matriz[i][j] * escalar)
        resultado.append(linha)
    return resultado

def exibir_matriz(matriz,tamanho):
    print("\nMatriz {tamanho}x{tamanho}!")
    t = tamanho
    print("-" * 25)
    for linha in matriz:
        for num in linha:
            print(f"|{num:5d}|", end =" ")

def main():
    tamanho = int(input("Digite o Tamanho da Matriz: "))

    ma = criar_matriz(tamanho)

    escalar = int(input("Digite o escalar para a Multiplicação: "))

    matriz_resultado = multiplicar_por_escalar(ma, escalar,tamanho)
    
    print ("\nMatriz Original:")
    exibir_matriz(ma, tamanho)
    print (f"\nEscalar: {escalar}")

    print("\nMatriz Resultado: ")
    exibir_matriz(matriz_resultado, tamanho)
 
if __name__ == "__main__":
    main()