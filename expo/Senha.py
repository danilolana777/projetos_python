import time
import sys
import shutil
import os

# Forçar o terminal a ter largura e altura maior
os.system("mode con: cols=120 lines=30")

# C.E.L.I.A. – (Código Experimental de Lógica e Inteligência Artificial)

senhas = {
    1: "01101001",
    2: "root42",
    3: "C3L1A",
    4: "firewalldown",
    5: "synt4xerr0r",
    6: "overclock99"
}

senhas_descobertas = [False] * 6

def centralizar(msg):
    largura = shutil.get_terminal_size().columns
    print(msg.center(largura))

def efeito_processando(mensagem="Processando"):
    for i in range(3):
        print(f"\r{mensagem}{'.'*i}  ", end="")
        time.sleep(0.5)
    print("\r", end="")

def senha_input(n):
    tentativa = input(f"\nDigite a senha {n}: ")
    efeito_processando("C.E.L.I.A. analisando")
    if tentativa == senhas[n]:
        senhas_descobertas[n-1] = True
        centralizar("\033[32mSenha CORRETA! Chave de segurança desbloqueada.\033[0m")
    else:
        centralizar("\033[31mSenha incorreta!\033[0m")

def verificar_vitoria():
    if all(senhas_descobertas):
        centralizar("\n\033[95mALERTA MÁXIMO: TODAS AS CHAVES LOCALIZADAS!\033[0m")
        time.sleep(1)
        centralizar("\033[92mSistema de contenção ativado... C.E.L.I.A. está sendo desligada!\033[0m")
        efeito_processando("Encerrando processos maliciosos")
        centralizar("\033[92m>>> CONCLUÍDO <<<\033[0m")
        return True
    return False

def menu():
    centralizar("="*50)
    centralizar("CENTRO TÉCNICO EDUCACIONAL - TERMINAL DE CONTENÇÃO")
    centralizar("="*50)
    print()
    centralizar("Vocês precisam encontrar as 6 senhas para retomar o controle.\n")
    
    for i in range(6):
        if not senhas_descobertas[i]:
            centralizar(f"{i+1}. Inserir Senha {i+1}")
        else:
            centralizar(f"{i+1}. Senha {i+1} [DESBLOQUEADA]")
    
    centralizar("7. DESISTIR")
    
    try:
        opc = int(input("\nDigite uma das operações (1-7): "))
        if opc < 1 or opc > 7:
            centralizar("\033[31m---Digite um Número entre 1 a 7!---\033[0m")
            return False
    except ValueError:
        centralizar("\033[31mEntrada Inválida! Digite um número.\033[0m")
        return False
    
    if opc >= 1 and opc <= 6 and senhas_descobertas[opc-1]:
        centralizar(f"\033[33mSenha {opc} já foi desbloqueada, escolha outra opção.\033[0m")
        return False
    
    if opc == 7:
        centralizar("\033[31m---Programa encerrado! DERROTA---\033[0m")
        return True

    senha_input(opc)
    return verificar_vitoria()

if __name__ == "__main__":
    # Tela inicial simples
    centralizar("\033[36mIniciando terminal de contenção...\033[0m")
    time.sleep(1)
    sair = False
    while not sair:
        sair = menu()

