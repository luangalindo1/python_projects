# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

import random
from os import system

estados_capitais = {'AC': 'Rio Branco', 'AL': 'Maceió', 'AP': 'Macapá', 'AM': 'Manaus', 
                    'BA': 'Salvador', 'CE': 'Fortaleza', 'DF': 'Brasília', 'ES': 'Vitória', 
                    'GO': 'Goiânia', 'MA': 'São Luís', 'MT': 'Cuiabá', 'MS': 'Campo Grande', 
                    'MG': 'Belo Horizonte', 'PA': 'Belém', 'PB': 'João Pessoa', 'PR': 'Curitiba', 
                    'PE': 'Recife', 'PI': 'Teresina', 'RJ': 'Rio de Janeiro', 'RN': 'Natal', 
                    'RS': 'Porto Alegre', 'RO': 'Patrocínio', 'RR': 'Boa Vista', 
                    'SC': 'Florianópolis', 'SP': 'São Paulo', 'SE': 'Aracaju', 'TO': 'Palmas'}

acertos = 0
erros = 0
cont = 's'

while cont == 's':
    system("clear")
    estado = random.choice(list(estados_capitais.keys()))
    resp = input('\nQual é a capital do Estado {}? -> '.format(estado))
    if resp == estados_capitais[estado]:
        print('\nResposta correta!')
        acertos += 1
    else:
        print('\nErrado!\nA resposta era {}.'.format(estados_capitais[estado]))
        erros += 1
    cont = str(input("\nQuer continuar? [s/n] ")).strip().lower()
print("\nVocê teve {} acertos e {} erros.".format(acertos, erros))
print("Um aproveitamento de {:.2f}%\n".format((acertos / (acertos + erros) * 100)))