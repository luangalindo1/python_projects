import random
import os

cont = 1
win = 0
lose = 0
while cont == 1:
    os.system('cls')
    print("====================================")
    print("Bem vindo ao Pedra, Papel e Tesoura")
    print("====================================")
    print("\nAs escolhas são: 1 - Pedra, 2 - Papel, 3 - Tesoura")
    print("\nPlacar: Jogador {} x Computador {}".format(win, lose))
    esc = int(input("\nInsira seu jogo: "))
    while esc not in [1, 2, 3]:
        esc=int(input("Escolha inválida! Insira novamente: "))
    esc_pc = random.randint(1, 3)
    print ("A escolha do computador foi: {}".format(esc_pc))
    if esc == esc_pc:
        print("\nEmpate!")
    elif (esc == 1 and esc_pc == 3) or (esc == 2 and esc_pc == 1) or (esc == 3 and esc_pc == 2):
        win+=1
        print("\nVocê venceu!")
    else:
        lose+=1
        print("\nVocê perdeu!")
    cont = int(input("\nDeseja continuar? 1 - Sim, 0 - Não: "))
    while cont not in [0, 1]:
        cont = int(input("Escolha inválida! Insira novamente: "))
    os.system('cls' if os.name == 'nt' else 'clear') #Limpar a tela no windows ou linux    
    print("\nPlacar: Jogador {} x Computador {}\n".format(win, lose))