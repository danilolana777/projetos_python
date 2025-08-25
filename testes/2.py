import random
print ("ADIVINHE O NÚMERO CERTO ENTRE 1 E 100")
n = random.randint(1, 100)
cont = 1
aviso = ("Digite um número entre 1 E 100!")
while cont < 11:
    try:
        x = int(input("Palpite:"))
        cont +=1
        if x > 100 or x < 1:
            cont -= 1
            print(aviso)
        else:
            if x < n:
                print ("Número Maior!")
            if x > n:
                print("Número Menor!")
            if x == n:
                print(f"Você Acertou na tentativa {cont}! Parabéns")
                break
    except ValueError:
       print (aviso)
    con = 11 - cont
    if cont == 11:
        print ("Acabaram as Tentativas!")
    if cont < 11: 
        print(f"Restam {con} Tentativas!")
    