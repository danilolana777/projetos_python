matriz = []
valor = 0
for i in range(4):
    linha = []
    for j in range(4):
        valor += 1 
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print (linha)