arquivo = open("arquivos/arquivo.txt", "w")
arquivo.write("Substituindo o conteúdo do arquivo.")
arquivo.close()

arquivo = open("arquivos/arquivo.txt", "r")
for linha in arquivo:
    print(linha)

arquivo.close()
