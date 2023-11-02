# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

import random

segredo = random.randint(1, 100)
tentativas = 0
while tentativas < 3:
    chute = int(input("\nTente adivinhar o número: "))
    if segredo == chute:
        print("\nParabéns você acertou!!")
        break
    elif segredo < chute:
        print("\nO seu chute foi maior que o número gerado.")
    else:
        print("\nO seu chute foi menor que o número gerado.")
    tentativas+=1
print("\nO número gerado foi {}".format(segredo))