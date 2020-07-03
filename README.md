PERFIL DE VARREADURA
Script de automação ArcMap
Autores: luischerem | gabrielalmeida

A funcionalidade deste script é realizar uma integração com ArcMap(ArgGis) para análises de perfis topográficos a partir de dados georreferenciados.
O pacote do arcpy integra diversas funcionalidades utilizadas para finalidades diversas.

#importação do módulo arcpy
import arcpy

Além do módulo arcpy o script comtepla o uso de bibliotécas python como matplotlib (para plotagem de gráficos de perfil), numpy (para geomática dos dados),
pandas (para integração com ciência de dados e ArcMap) dentre outros módulos nativos

#importação dos módulos para ciência de dados
import matplotlib
import numpy as np
import pandas as pd

VARIÁVEIS
#variáveis (a critério de modificação)
PATH_RASTER = "c:\\path\to\file\\file" #(caminho do raster)
DATA_X = [] #array matriz X
DATA_Y = [] #array matriz Y

#... Outras variáveis

A TOOLBOX
A toolbox é excencial para acoplagem do script python ao ArcMap (ArcGis), uma vez que essa fará interface com o script.

#Variáveis para a toolbox inputs outputs
#Buscar parametros de entrada
inRaster1  = arcpy.GetParameterAsText(0)
outDatas1  = arcpy.GetParameterAsText(1)
outSHP1    = arcpy.GetParameterAsText(2) #required = none


O CSV
O csv é um tipo de arquivo muito comum em ciência de dados, para tal o script gera arquivos csv com a finalidade de avaliação dos dados para uma plotagem final
outDatas1  = arcpy.GetParameterAsText(1) #gera o csv a partir dos dados recuperados por numpy


CONSIDERAÇÕES FINAIS
O script apesar de simples é útil à medida em que automatiza uma tarefa maçante em python.
