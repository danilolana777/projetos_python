import random

acerto = ("\n\033[32mAcerto\033[0m")
erronum = ("\n\033[31mDigite um Número!\033[0m")
perda = ("\033[31m\nAs tentativas acabaram!\033[0m")
maior = ("\n\033[33mNúmero Maior\033[0m")
menor = ("\n\033[35mNúmero Menor!\033[0m")
def menu():
    print ("\n", 15*"=", "\n  Jogo Adivinha!\n", 15*"=",)
    return fase1()

def fase1():
    print("\n\033[32mPrimeira-Fase\033[0m\n==Número de 1 a 100==")
    print("\nVocê tem 10 Tentativas!")
    n = random.randint(1, 100)
    rt = 0
    while True:
        try:
        
            t = int(input("Tentativa: "))
            if t <= 100 and t >= 1:
                if n < t:
                    print(menor)
                    rt += 1
                elif t < n:
                    print(maior)   
                    rt += 1
                else:
                    print(acerto)
                    print (f"\nVocê acertou na tentativa {rt + 1}!")
                    print("\nPassando para segunda fase!")
                    return fase2()
            else:
                print("\n\033[31mDigite um Número de 1 a 100!\033[0m")
            
            rt2 = 10 - rt
            if rt < 10:
                print (f"\nRestam {rt2} tentativas!")
                
            else:
                print (perda)
                print (f"\nO número era: {n}")
                return menu()
        except ValueError:
            print (erronum)

def fase2():
    print("\n\033[32mSegunda-Fase\033[0m\n==Número de 1 a 1000==")
    print("\nVocê tem 10 Tentativas!")
    n = random.randint(1, 1000)
    rt = 0
    while True:
        try:
        
            t = int(input("Tentativa: "))
            if t <= 1000 and t >= 1:
                if n < t:
                    print(menor)
                    rt += 1
                elif t < n:
                    print(maior)   
                    rt += 1
                else:
                    print(acerto)
                    print (f"\nVocê acertou na tentativa {rt + 1}!")
                    print("\nPassando para terceira fase!")
                    return fase3()
            else:
                print("\n\033[31mDigite um Número de 1 a 1000!\033[0m")
            
            rt2 = 10 - rt
            if rt < 10:
                print (f"\nRestam {rt2} tentativas!")
                
            else:
                print(perda)
                print (f"\nO número era: {n}")
                return menu()
        except ValueError:
            print (erronum)

def fase3():
    print("\n\033[32mTerceira-Fase\033[0m\n==Número de 1 a 10.000==")
    print("\nVocê tem 12 Tentativas!")
    n = random.randint(1, 10000)
    rt = 0
    while True:
        try:
        
            t = int(input("Tentativa: "))
            if t <= 10000 and t >= 1:
                if n < t:
                    print(menor)
                    rt += 1
                elif t < n:
                    print(maior)   
                    rt += 1
                else:
                    print(acerto)
                    print (f"\nVocê acertou na tentativa {rt + 1}!")
                    return fim()
            else:
                print("\n\033[31mDigite um Número de 1 a 10.000!\033[0m")
            
            rt2 = 12 - rt
            if rt < 12:
                print (f"\nRestam {rt2} tentativas!")
                
            else:
                print(perda)
                print (f"\nO número era: {n}")
                return menu()
        except ValueError:
            print (erronum)
    

def fim():
    print("\n\033[34mParabéns você ganhou o jogo!\033[0m")
    d = input("Dejesa tentar novamente? Digite (s) para sim e (n) para não: ").strip()
    if d.lower() == "s":
        menu()
    elif d.lower() == "n":
        print ("\n\033[33m-----Programa-Encerrado-----\033[0m")

menu()