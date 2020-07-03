#--------------------------------------
#perfil_de_varredura.py
#direção do projeto:     luischerem        luis.cherem@gmail.com
#programação e direção:  gabrielalmeida    gabriel.almeida@uft.edu.br
#arcmap arqgis
#--------------------------------------

import arcpy
import subprocess
import matplotlib.pyplot as plt
import numpy

#matrizes
DATA_X_DISTANCES  = []
DATA_Y_ELEVATIONS = []

#variáveis locais e de uso da toolbox arcmap
PATH_RASTER = arcpy.GetParameterAsText(0)
EXIT_DATAS  = arcpy.GetParameterAsText(1)

#saídas em formatos
profileFolder  = EXIT_DATAS
profilePrefix  = "ArcPy_"
profilePostfix = "graph_profile"

def main():
	"""
	main function for project
	"""
	return 0

def multipleGraphsProfile():
	#ATENÇÃO: FUNÇÃO PARA ESTUDO NÃO ASSUME O PROJETO FINAL
	#ESSA FUNÇÃO TEM COMO OBJETO A PLOTAGEM DE MULTIPLOS GRÁFICOS
	#PARA FINALIDADES DIVERSAS
	#AJUSTADA VIA TOOLBOX DO ARCMAP

		data = []
	for i in range(0, 5000):
	    data.append([i, float(i + random.randrange(-50, 50))/100, 5])

	pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
	cnt = 0
	figs = plt.figure()
	for data_chunk in chunks(data, 600):
	    plot_num = 321
	    fig = plt.figure(figsize=(10, 10))
	    for sub_chunk in chunks(data_chunk, 100):
	        cnt += 1
	        d = [a[0] for a in sub_chunk]
	        z = [a[1] for a in sub_chunk]
	        zv = [a[2] for a in sub_chunk]

	        print plot_num
	        plt.subplot(plot_num)

	        #plotar perfile e definir estilos
	        plt.plot(d,z,'r',linewidth=0.75)
	        plt.plot(d,z,'ro',alpha=0.3, markersize=3)
	        plt.plot(d,zv,'k--',linewidth=0.5)
	        plt.xlabel('Distancia de inicio')
	        plt.ylabel('Elevação')
	        plt.title('Perfil {0} python e matplotlib'.format(cnt))

	        #modificar fonte
	        plt.rcParams.update({'font.size': 8})
	        plot_num += 1

	    pdf.savefig(fig)

	pdf.close()

def validationDatas():
	"""
	validation datas for raster data or shp files
	"""
	return 0

#...

if __name__ == "__main__":
		main()