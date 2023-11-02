# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

import random
import string
from os import system
system("clear")
valores = []
palavras = []
soma = 0
media = 0

# Gerando valores aleatórios
for _ in range(5):
    valores.append(random.randint(0, 100))
maior = valores[0] # Instanciando o valor inicial arbitrariamente
print(valores)

# Gerando palavras aleatórias
for _ in range(5):
    tamanho = random.randint(3, 10)
    string_aleatoria = ''.join(random.choice(string.ascii_letters) for _ in range(tamanho))
    palavras.append(string_aleatoria)
print(palavras)

# Soma e média e maior valor
for num in valores:
    soma += num
    if num >= maior:
        maior = num
media = soma/len(valores)
print("\nA soma vale {}, a média vale {}".format(soma, media))
print("e o maior valor é {}\n".format(maior))

# Palavras com mais de 5 letras
for palavra in palavras:
    if len(palavra) > 4:
        print(palavra)