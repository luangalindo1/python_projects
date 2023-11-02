# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.
#%% Bibliotecas
import os
#%% Dados a serem comparados
usuario_padrao = input("Insira um nome de usuário: ")
senha_padrao = input("Insira uma senha: ")
os.system("clear")

#%% Início do teste
nome_usuario = input("Digite seu nome de usuário: ")
if (nome_usuario == usuario_padrao):
    senha = input("Insira sua senha: ")
    if(senha == senha_padrao):
        print("\n\033[1;32mSenha correta!\033[m")
    else:
        print("\n\033[1;41mSenha inválida.\033[m")
else:
    print("\n\033[1;41mUsuário inválido.\033[m")
# %%
