PERFIL DE VARREADURA
Script de automação ArcMap
luis cherem
gabriel almeida
daniel santos

A funcionalidade deste script é realizar uma integração com ArcMap(ArgGis) para análises de perfis topográficos a partir de dados georreferenciados.
O pacote do arcpy integra diversas funcionalidades utilizadas para finalidades diversas.

"Basicamente, todos os modelos estão errados, mas alguns são uteis" - George Box

#importação do módulo arcpy
import arcpy


VARIÁVEIS
#variáveis (a critério de modificação)
in_raster     = "" #raster principal
in_mask_data  = "" #poligono
meu_ambiente  = "C:\\users\\user\\path\\to\\database.gdb"
#... Outras variáveis

#Variáveis para a toolbox inputs outputs
#Buscar parametros de entrada
inRaster1  = arcpy.GetParameterAsText(0)
outDatas1  = arcpy.GetParameterAsText(1)
outSHP1    = arcpy.GetParameterAsText(2) #required = none

Processamento e automação do perfil:
#extrair a mascara
out_extract_mask = ExtractByMask(in_raster, in_mask_data)
#realizar o calculo a partir da mascara
RM_mde_minus = out_extract_mask * -1
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
    
    
...
