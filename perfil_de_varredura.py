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

try:
    outextract_mask = ExtractByMask(in_raster, in_mask_data)
    RE_mde_minus = out_extract_mask * -1
    FD_mde_minus = arcpy.sa.FlowDirection(RE_mde_minus)
    SK_mde_minus = arcpy.sa.Sink(FD_mde_minus)
    pnt_mde_min  = arcpy.RasterToPoint_conversion(SK_mde_minus, "pnt_mde_min")
    pnt_mde_top1 = arcpy.sa.ExtractValuesToPoints(pnt_mde_min, RE_mde_minus, "pnt_mde_top1")#passível de erro
    pnt_mde_3d   = arcpy.FeatureTo3DByAttribute_3d("pnt_mde_top1", "pnt_mde_3d", "RASTERVALU")
except arcpy.ExecuteError:
    print(arcpy.GetMessages())
    exit("Erro ao interpolar pontos!!, Verifique os arquivos!!")
