import os
import random
import string

# Criaremos arquivos aleatórios para a função
def random_files():
    # Lista com extensões
    ext = ['.txt', '.docx', '.xlsx', '.pptx', '.pdf']
    for _ in range(5):
        # Gerando nomes aleatórios para os arquivos com 5 caracteres
        nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        ext_random = random.choice(ext)
        nome_arq = nome + ext_random
        with open(nome_arq, 'w') as f:
            f.write('Este é um arquivo aleatório')

random_files()
# Tomando caminho do diretório atual
current_path = os.getcwd()

# Listando todos os arquivos dentro do diretório
full_list = os.listdir(current_path)

# Separando a lista de arquivos dos arquivos .py e de outras pastas
files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]

# Separando as extensões dos arquivos, com o cuidado de não usar
# elementos repetidos
types = list(set([i.split('.')[1] for i in files_list]))

# Criando diretórios para cada extensão
for ftype in types:
    os.mkdir(ftype)

# Movendo os arquivos para pastas com base em sua extensão
for file in files_list:
    from_path = os.path.join(current_path, file) 
    to_path = os.path.join(current_path, file.split('.')[-1], file)
    os.replace(from_path, to_path)