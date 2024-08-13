import os
from scrapperXML import *
import cProfile
import pstats

prof = cProfile.Profile()

def scanning():
    """
    VARRE O DIRETÓRIO DE CURRÍCULOS LATTES E BUSCA TODOS OS CURRÍCULOS ZIPADOS

    Descrição: Caminha o diretório atual até os arquivo zips e chama a 
    função openCurriculo(curriculo) passando como parâmetro o currículo zipado

    Parâmetro: Nenhum

    Retorno: Nenhum
    """
    diretorioAtual = os.getcwd() #pegando o diretório atual

    diretorioCurriculos = os.path.join(diretorioAtual, "repo") #pegando o diretório dos currículos
    listaDeSubDiretorios = os.listdir(diretorioCurriculos) #gerando lista de subdiretórios para serem iteradas

    #iterando lista de subdiretorios
    for subdiretorio in listaDeSubDiretorios:
        subdiretorio = os.path.join(diretorioCurriculos, subdiretorio) #pegando o caminho de cada subdiretório
        curriculos = os.listdir(subdiretorio) #lista de curriculos de cada subdiretório

        #iterando a lista de curriculos
        for curriculo in curriculos:
            curriculo = os.path.join(subdiretorio, curriculo) #pegando o caminho para o currículo Zipado

            prof.enable()
            openCurriculo(curriculo) #Chamando função de abertura de arquivo
            prof.disable()
            break

        break #BREAK temporário só para percorrer até o subdiretório 01
scanning()  

stats = pstats.Stats(prof).sort_stats('cumtime')
stats.print_stats()