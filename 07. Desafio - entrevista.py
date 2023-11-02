# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

from datetime import datetime

nome = input("Insira seu nome: ")
print("Olá, {}".format(nome.split()[0]))
print("Seu nome completo possui {} caracteres".format(len(nome)))
idade = int(input("Quantos anos você tem? "))
print("Você terá {} anos em {}.".format(idade + 5, datetime.now().year + 5))
