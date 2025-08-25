import random
def criar_matriz(tamanho):
    return [[random.randint(0,50)for _ in range(tamanho)]for _ in range(tamanho)]


def exibir_matriz(matriz):
    print("\nMatriz 4x4:")
    print("-" * 25)
    for linha in matriz:
        for num in linha:
            print(f"|{num:3d}|", end=" ")
        print()
    print("-" * 25)


def soma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))
  


def soma_diagonal_secundaria(matriz):
    tamanho = len(matriz) 
    print()
    return sum(matriz[i][tamanho-1-i] for i in range (tamanho))
      


tamanho = 4
matriz = criar_matriz(tamanho)
exibir_matriz(matriz)
print (f"\nA Soma da Diagonal Principal é de: {soma_diagonal_principal(matriz)}")
print (f"A Soma da Diagonal Principal é de: {soma_diagonal_secundaria(matriz)}")
