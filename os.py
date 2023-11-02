import os

# Mostra o caminho completo do diretório atual
os.getcwd()

# Retorna uma lista contendo todos os arquivos de determinada pasta
os.listdir()
os.listdir('C:\\Users\\luang\\OneDrive\\Documentos\\_GÁS INFINITO\\ENGENHARIA ELÉTRICA\\_Cursos\\Asimov\\1. Python Starter\\5. Módulo OS')

# os.chdir() - Troca o diretório atual
actual_dir = os.getcwd()
print(os.getcwd())
os.chdir('C:\\Users\\luang\\OneDrive\\Documentos\\_GÁS INFINITO\\ENGENHARIA ELÉTRICA\\_Cursos\\Asimov\\1. Python Starter')
print(os.getcwd())
os.chdir(actual_dir)

# Cria uma pasta.
os.mkdir('Pasta1')

# Criar um arquivo
f = open('arqteste1.txt', 'w')
f.close()

# Renomeia um arquivo
os.rename('Pasta1', 'Pasta2')

# Deleta arquivo. Não deleta pastas.
os.remove('arqteste1.txt')

# Deleta uma pasta.
os.rmdir('Pasta2')

# Executa um comando de shell
cmd = 'date'
os.system('date')
