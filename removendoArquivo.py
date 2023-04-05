#Importando módulo "os"
import os

if os.path.exists("arquivos/novoArquivo1.txt"):
    os.remove("arquivos/novoArquivo1.txt")
else:
    print("Arquivo não existe!")