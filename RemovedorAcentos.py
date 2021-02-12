import sys
import os
import unicodedata


def arquivos(nome_arquivo_fonte, nome_arquivo_destino):
    retorno = True

    if nome_arquivo_fonte.strip(" ") == "":
        print("Arquivo texto fonte não informado !")
        retorno = False

    if retorno is True and os.path.isfile(nome_arquivo_fonte) is False:
        print("Arquivo texto fonte não encontrado !")
        retorno = False

    if retorno is True and nome_arquivo_destino.strip(" ") == "":
        print("Arquivo texto destino não informado !")
        retorno = False

    if retorno is True and os.path.dirname(os.path.abspath(os.path.basename(nome_arquivo_destino))) != "" and \
            os.path.isdir(os.path.dirname(os.path.abspath(nome_arquivo_destino))) is False:
        print("Diretório do arquivo texto destino não encontrado !")
        retorno = False

    return retorno


def remove_acentos(texto_com_acento):
    nfkd = unicodedata.normalize('NFKD', texto_com_acento)
    texto_sem_acento = u"".join([i for i in nfkd if not unicodedata.combining(i)])
    return texto_sem_acento


def executar(nome_arquivo_fonte, nome_arquivo_destino):
    if nome_arquivo_fonte.strip(" ") == "" and nome_arquivo_destino.strip(" ") == "":
        for i, parametro in enumerate(sys.argv):
            if i == 1:
                nome_arquivo_fonte = parametro
            elif i == 2:
                nome_arquivo_destino = parametro

    if arquivos(nome_arquivo_fonte, nome_arquivo_destino) is True:
        arquivo_destino = open(nome_arquivo_destino, mode="w", encoding='utf-8')
        print("Criado o arquivo texto destino " + os.path.basename(nome_arquivo_destino) + " em " + os.path.dirname(os.path.abspath(os.path.basename(nome_arquivo_destino))) + ".")
        arquivo_fonte = open(nome_arquivo_fonte, mode="r", encoding='utf-8')
        print("Aberto o arquivo texto fonte " + os.path.basename(nome_arquivo_fonte) + " em " + os.path.dirname(os.path.abspath(os.path.basename(nome_arquivo_fonte))) + ".")
        while True:
            linha = arquivo_fonte.readline()
            if linha:
                arquivo_destino.writelines(remove_acentos(linha))
            else:
                break

        arquivo_fonte.close()
        print("Fechado o arquivo texto fonte !")
        arquivo_destino.close()
        print("Fechado o arquivo texto destino !")
        print("Concluído !")

executar("", "")