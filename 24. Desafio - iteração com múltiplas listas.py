# Dado duas listas, printe todos os valores que aparecerem
# comuns nas duas listas.

# Dado duas listas, printe uma mensagem dizendo se eiiste
# algum elemento em comum entre elas ou não.

import random
from os import system

system("clear")

lista1 = []
lista2 = []

for _ in range(10):
    lista1.append(random.randint(0, 10))
    lista2.append(random.randint(0, 10))
print("\nLista 1:", lista1)
print("\nLista 2:", lista2)

comuns = list(set(lista1).intersection(lista2))
if comuns:
    print("\nValores em comum: ", comuns)
else:
    print("\nNão existem valores em comum.")

def duplicados(lista):
    unicos = set(lista)
    if len(lista) == len(unicos):
        return []
    else:
        return  [i for i in lista if lista.count(i) > 1]

dupli1 = duplicados(lista1)
dupli2 = duplicados(lista2)
if dupli1:
    print("\nExistem valores repetidos na primeira lista: ", dupli1)
if dupli2:
    print("\nExistem valores repetidos na segunda lista: ", dupli2)