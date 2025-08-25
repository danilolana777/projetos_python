matriz =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [1,14,15,16]
]
print ("Matriz 4x4 em grade")
soma = 0

for i in range(len(matriz)):
    soma += matriz[i][i]

print("A soma da principal vale:", soma)

s = 0
diagonal_secundaria = []
for j in range(len(matriz)):
    diagonal_secundaria.append(matriz[j][3 - j])
    s += matriz[j][3 - j]

print("Elementos da diagonal secundaria: ", diagonal_secundaria)
print("A soma da principal vale:", s)

print ("A soma da diagonal secundária vale:", s)
if soma > s:
    print(f"A soma {soma} é maior que {s}")
elif soma < s:
    print(f"A soma {s} é maior que {soma}")
elif soma == s:
    print(f"As somas {s} e {soma} são iguais")