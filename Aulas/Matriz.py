import random
matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]
print ("Matriz 3x3 em Grade:")
for row in matrix:
    for num in row:
        print (f"[{num:3d}]", end=" ")
    print()
print ("\nMatrix 3x3 em linha, sem formatação: ")
for row in matrix:
    for num in row:
        print (f"[{num:3d}]", end=" ")
