try:
    novoArquivo = open("arquivos/novoArquivo2.txt", "x")
    novoArquivo.write("Adicionando conteúdo dentro do arquivo!")
    novoArquivo.write("""
    Adicionando várias linhas.
    Com as aspas triplas.
    Para ver se o arquivo salva com esse formato e quebras de linhas.
    """)
except:
    print("\033[7;35;46mArquivo já existe!\033[m")