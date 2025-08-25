
senha_correta = "1234"
senha = input("Digite a Senha:")
cont = 1
while senha != senha_correta and cont < 3:
    senha = input("Senha errada, Digite a Senha Correta:")
    cont += 1
if cont == 3 and senha_correta != senha:
    print ("Tentativas Excedidas")
    conf = input("Digite 'ABCD' para continuar:")
    if conf != ("ABCD"):
        print ("Acesso bloqueado:")
    elif conf == ("ABCD"):
        print("Novas Tentativas Concedidas")
        ns = input("Digite a Senha, Você tem uma tentativa:")
        if ns != senha:
            print("Acesso Bloqueado")
else:
    print ("A senha está correta!")
