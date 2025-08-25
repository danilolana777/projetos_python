def ex1():
    print("Bem vindo ao Mundo das Funções!")


def ex2():
    return "Olá Mundo"


def ex3(nome):
    print (f"Nome do Aluno: {nome}")


def ex4():
    return 10


def ex5():
    print ("Primeira\nSegunda\nTerceira")


def ex6(a, b):
    print (a + b)


def ex7(nome):
    print (f"Olá, {nome}! Seja Bem-Vindo!")


def ex8(base, altura):
    print ("base X altura = ", base * altura)

def ex9(numero):
    n1 = (numero % 2)
    if n1 == 0:
        print("Número Par")
    else:
        print("Número Ímpar")


def ex10(n1, n2, n3):
    return (n1 + n2 + n3) /3 
media = ex10(5, 10, 6)


def ex11(a, b, c):
    if a > b and a > c:
        print(f"{a} é maior")
    elif b > a and b > c:
        print(f"{b} é maior")
    else:
        print(f"{c} é maior")


def ex12(c):
    print ((c * 9/5) + 32 )

lista = [1, 2 ,3 ,4, 50]
def ex13(lista):
    return (sum(lista))


def ex14(lista):
    pares = 0
    for num in lista:
        if(num % 2 == 0):
            pares += 1
    return pares

lista = [1, 2, 3, 4, 5, 6, 7, 8]

def ex15(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado



def ex152(base, expoente):

    print (base ** expoente)

def ex16(numero, digito):
    contador = 0
    for caracter in str(numero):
        if caracter == str(digito):
            contador += 1
    return contador

def ex17(numero):
    return sum(int(c) for c in str(numero))

    
def ex18(numero):
    fat = 1
    for i in range(1, numero + 1):
        fat *= i
    return fat

def ex19():
    lista = [ 9, 4, 6, 2, 5, 3, 1, 8, 7, 10]
    lista2 = sorted(lista)
    return lista2

def ex20():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lreverse = lista[::-1]
    strings = ("!ovideR suetaM álO")
    sreverse = strings[::-1]
    print (sreverse)
    print (lreverse)
