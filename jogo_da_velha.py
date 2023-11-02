#%% Bibliotecas
import random
import os

#%% Primeira Classe
class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)] # inicializa o tabuleiro vazio

    def imprimir_tabuleiro(self):
        os.system("clear") # cls for windows
        for i in reversed(range(0, 9, 3)):
            print('| ' + self.tabuleiro[i] + ' | ' + self.tabuleiro[i+1] + ' | ' + self.tabuleiro[i+2] + ' |')
            print('-------------')

    def jogada_valida(self, posicao):
        return self.tabuleiro[posicao] == ' '

    def vitoria(self, jogador):
        vitoria_condicoes = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for condicao in vitoria_condicoes:
            if self.tabuleiro[condicao[0]] == self.tabuleiro[condicao[1]] == self.tabuleiro[condicao[2]] == jogador:
                return True
        return False
    def jogar(self):
        while True:
            self.imprimir_tabuleiro()
            posicao_jogador = int(input("Sua vez! Escolha uma posição de 1 a 9: ")) - 1
            while posicao_jogador not in range(0, 9):
                posicao_jogador = int(input("Por favor, digite um número entre 1 e 9:")) - 1
            if self.jogada_valida(posicao_jogador):
                self.tabuleiro[posicao_jogador] = 'X'
                if self.vitoria('X'):
                    self.imprimir_tabuleiro()
                    print("Parabéns! Você ganhou!")
                    return
            else:
                print("Posição inválida. Tente novamente.")
                continue

            posicao_computador = random.choice([i for i in range(9) if self.jogada_valida(i)])
            self.tabuleiro[posicao_computador] = 'O'
            if self.vitoria('O'):
                self.imprimir_tabuleiro()
                print("O computador ganhou!")
                return

#%% Iniciar Jogo
if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
