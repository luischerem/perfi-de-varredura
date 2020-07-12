"""
perfil_de_varredura.py
script de automação para arcmap

luis cherem     luis.cherem@gmail.com
gabriel almeida gabriel.almeida@uft.edu.br
daniel santos   daniel.A.Sants@hotmail.com
"""
import arcpy
import os
from arcpy.sa import *
from arcpy import env

#setar o ambiente de trabalho e variaveis
in_raster     = "" #raster principal
in_mask_data  = "" #poligono

meu_ambiente  = "C:\\users\\user\\path\\to\\database.gdb"
env.workspace = meu_ambiente
if env.workspace:
    print("Ambiente: ", env.workspace)
else:
    print("É importante setar seu ambiente: C:\\users\\user\path\to\ambiente.gdb")
    exit()
    
#extrair a mascara
out_extract_mask = ExtractByMask(in_raster, in_mask_data)
#realizar o calculo a partir da mascara
RE_mde_minus = out_extract_mask * -1
#hydrology -> flow direction
FD_mde_minus = arcpy.sa.FlowDirection(RE_mde_minus)
#hydrology -> sink
SK_mde_minus = arcpy.sa.Sink("FD_mde_minus")
#converter raster para pontos
pnt_mde_min  = arcpy.RasterToPoint_conversion(SK_mde_minus,
    meu_ambiente+"\\raster-point")
#tentar extrair valores de pontos do raster
try:
    pnt_mde_top1 = arcpy.sa.ExtractValuesToPoints(pnt_mde_min, in_raster,
        meu_ambiente+"\\pnt_mde_top1",
        "INTERPOLATE", "VALUE_ONLY")#passível de erro
except:
    exit("Erro ao interpolar pontos!!, Verifique os arquivos!!")
