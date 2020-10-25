# Librerias
import sys, os
import numpy as np
import pandas as pd

# Librerias
from codigo.analisis import gen_dicc_con_pals_y_verbs
from codigo.vectorization import gen_vectores_xy
from codigo.clasificacion import gen_vector_raw

# Graficos
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

# Función de tokenización
def leer_stop_words (archivo):
	# Variables
	stop_words = []
	# Leer documento
	with open(archivo, 'r', encoding="utf-8") as myFile: # open(archivo, encoding="latin-1")
		# Recuperar lineas del texto
		lins_arch = myFile.readlines()
		contador = 1
		# Recorrer parrafos del archivo
		for palabra in lins_arch:
			# Limpiar y reducir texto
			palabra = palabra.strip().lower()
			# Validar si agregar palabra a stopwords
			if palabra not in stop_words:
				# Agregar palabra a stopwords
				stop_words.append(palabra)
	# Regresar lista de stopwords
	return stop_words

# Función para obtener arreglos X, Y, Z
def obtenerArreglos(panda_x, panda_y, panda_z, panda_w):
	# Arreglos
	x = []
	y = []
	z = []
	w = []
	# Recorrer arreglo
	for xrw in panda_x:
		# Recorrer sub arreglo
		for nx in xrw:
			# Agregar X
			x.append(nx)
	# Recorrer arreglo
	for yrw in panda_y:
		# Recorrer sub arreglo
		for ny in yrw:
			# Agregar X
			y.append(ny)
	# Recorrer arreglo
	for zrw in panda_z:
		# Recorrer sub arreglo
		for nz in zrw:
			# Agregar X
			z.append(nz)
	# Recorrer arreglo
	for wrw in panda_w:
		# Recorrer sub arreglo
		for nw in wrw:
			# Agregar X
			w.append(nw)
	# Regresar resultado
	return x, y, z, w

# Función para obtener arreglos X Y de porcentaje
def obtenerAryConPorcent(x, y):
	# Variables
	diccXY = {}
	nx = []
	ny = []
	total = 0
	# Recorrer Y
	for i in range(len(y)):
		# Validar
		if y[i] != 0:
			# Recupera valores
			tator = x[i]
			# Validar
			if tator not in diccXY:
				diccXY[tator] = 1
			else:
				diccXY[tator] += 1
	# Recirrer DiccXY
	for key, value in diccXY.items():
		# Armar array
		nx.append(key)
		ny.append(value)
		total += value
	# Recorrer Y
	for i in range(len(ny)):
		ny[i] = ny[i]/total
	# Regresar resultado
	return nx, ny

# Función para obtener arreglos X Y de porcentaje
def obtenerArySinCeros(x, y):
	# Variables
	diccXY = {}
	nx = []
	ny = []
	total = 0
	# Recorrer Y
	for i in range(len(y)):
		# Validar
		if y[i] != 0:
			# Armar array
			nx.append(x[i])
			ny.append(y[i])
	# Regresar resultado
	return nx, ny

# Función para obtener arreglos X Y Z de porcentaje
def obtenerArySinCeroXYZ(x, y, z):
	# Variables
	diccXY = {}
	nx = []
	ny = []
	nz = []
	total = 0
	# Recorrer Y
	for i in range(len(y)):
		# Validar
		if y[i] != 0:
			# Armar array
			nx.append(x[i])
			ny.append(y[i])
			nz.append(z[i])
	# Regresar resultado
	return nx, ny, nz

# Mostrar Scatterplot de datos
def mostrarScatterPlot3D (x, y, z):
	# Formatear arreglos
	nx, ny, nz = obtenerArySinCeroXYZ(x, y, z)
	# Definir figura contenedora
	figuraSP = plt.figure()
	ejeAx = figuraSP.gca(projection='3d')
	# ScatterPlot
	ejeAx.scatter(nx, ny, nz, c='r', marker='o')
	ejeAx.set_xlabel('X: ID del Autor')
	ejeAx.set_ylabel('Y: Valor IFIDF')
	ejeAx.set_zlabel('Z: ID Palabra')
	ejeAx.set_title('Scatter Plot 3D')
	plt.show()

# Mostrar Grafico de datos
def mostrarHistograma (ary_x):
	# Grafico
	sns.set_style('darkgrid')
	sns.distplot(ary_x)
	plt.xlabel('X: ID del Autor')
	plt.ylabel('Y: Valor IFIDF')
	plt.title('Histograma')
	plt.show()

# Mostrar Grafico de datos
def mostrarBoxPlot (ary_x):
	# Grafico
	sns.boxplot(ary_x)
	plt.title('BoxPlot')
	plt.show()

# Mostrar Grafico de datos
def mostrarHeatmap (ary_x):
	# Grafico
	sns.heatmap(data=ary_x, linewidth=0.5)
	plt.title('Heatmap')
	plt.show()

# Mostrar Grafico de datos
def mostrarArea (ary_x):
	# Grafico
	df = pd.DataFrame(np.array(ary_x), columns=['Valor IFIDF'])
	plot = df.plot.area()
	plt.title('Grafica de Area')
	plt.show ()

# Mostrar Scatterplot de datos
def mostrarScatterPlot2D (x, y):
	# Formatear arreglos
	nx, ny = obtenerArySinCeros(x, y)
	# ScatterPlot
	fig = plt.figure()
	plt.scatter(nx, ny, c='r')
	plt.xlabel('X: ID del Autor')
	plt.ylabel('Y: Valor IFIDF * 100')
	plt.title('Scatter Plot 2D')
	fig.savefig('./__graficas/graficaDispersión.png', dpi=300, quality=80, optimize=True, progressive=True)
	# plt.show()

# Mostrar Grafico de datos
def mostrarLineas (x, y):
	# Formatear arreglos
	nx, ny = obtenerArySinCeros(x, y)
	# Grafico
	fig = plt.figure()
	plt.plot(nx, ny)
	plt.xlabel('X: ID del Autor')
	plt.ylabel('Y: Valor IFIDF * 100')
	plt.title('Grafica de Lineas')
	fig.savefig('./__graficas/graficaLineas.png', dpi=300, quality=80, optimize=True, progressive=True)
	# plt.show()

# Mostrar Grafico de datos
def mostrarBarras (x, y):
	# Formatear arreglos
	nx, ny = obtenerArySinCeros(x, y)
	# Grafico
	fig = plt.figure()
	plt.bar(nx, ny)
	plt.xlabel('X: ID del Autor')
	plt.ylabel('Y: Valor IFIDF * 100')
	plt.title('Grafica de Barras')
	fig.savefig('./__graficas/graficaBarras.png', dpi=300, quality=80, optimize=True, progressive=True)
	# plt.show()

# Mostrar Grafico de datos
def mostrarPastel (x, y):
	# Formatear arreglos
	nx, ny = obtenerAryConPorcent(x, y)
	# Grafico ::::::::::::
	fig, ax = plt.subplots()
	ax.pie(ny, labels=nx, autopct='%1.1f%%')
	ax.axis('equal')
	plt.title('Grafica de Pastel')
	fig.savefig('./__graficas/graficaPastel.png', dpi=300, quality=80, optimize=True, progressive=True)
	# plt.show()

# Iniciar
if __name__ == "__main__":
	# Leer documento con StopWords
	listStopWords = leer_stop_words("./docs/stopwords-es.txt")

	# Documento # _m _all
	df = pd.read_csv('./docs/author_corpus_m.txt',
		sep = '\t',
		index_col = False,
		names = ["autor","texto"])

	# Remueve autor 5, que es igual al 4
	df = df[:][df['autor'] != 5]

	# Abstraer solo los parrafos
	X_raw = df['texto']

	# Generar vector de caracteristicas
	X_rw, Y_rw, Z_rw, W_rw, P_rw, Q_rw, A_rw = gen_vector_raw(listStopWords, df, X_raw, gen_vectores_xy, gen_dicc_con_pals_y_verbs)

	# Imprimir resultados
	x, y, z, w = obtenerArreglos(X_rw, Y_rw, Z_rw, W_rw)
	# x: Valor IFIDF
	# y: ID de Palabra
	# z: ID del Autor
	
	mostrarScatterPlot2D(z, x)	
	mostrarLineas(z, x)
	mostrarPastel(z, x)
	mostrarBarras(z, x)

	# ::: mostrarScatterPlot3D(z, x, y)
	# ::: mostrarHistograma(x)
	# ::: mostrarBoxPlot(x)
	# --- mostrarHeatmap(x)
	# mostrarArea(x)