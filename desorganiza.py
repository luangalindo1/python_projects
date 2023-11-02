import os

# Tomando caminho do diretório atual
current_path = os.getcwd()

# Listando as pastas
folders_list = [_ for _ in os.listdir(current_path) if os.path.isdir(_)]

# Movendo os arquivos para o diretório atual
for folder in folders_list:
    path = os.path.join(current_path, folder) 
    files = os.listdir(path)
    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(current_path, file)
        os.replace(from_path, to_path)
    os.rmdir(path)

# Deletando os arquivos que não são .py
# Listando todos os arquivos dentro do diretório
full_list = os.listdir(current_path)

# Separando a lista de arquivos dos arquivos .py e de outras pastas
kill_list = [_ for _ in full_list if os.path.isfile(_) and '.py' not in _]

# Finalmente removendo os arquivos
for file in kill_list:
    filepath = os.path.join(current_path, file) 
    os.remove(filepath)

# Ctrl K C comenta // Ctrl K U descomenta
# def delete_non_py_files(directory):
#     # Iterate over all files in the directory
#     for filename in os.listdir(directory):
#         # Get the file path
#         file_path = os.path.join(directory, filename)

#         # If the file is a directory, recursively call this function
#         if os.path.isdir(file_path):
#             delete_non_py_files(file_path)
#         # If the file is not a .py file, delete it
#         elif os.path.splitext(file_path)[1] != ".py":
#             os.remove(file_path)