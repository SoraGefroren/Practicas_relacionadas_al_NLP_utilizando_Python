# Librerias
import sys, os
import numpy as np
import pandas as pd
import random
from operator import itemgetter

# Librerias
from codigo.analisis import gen_dicc_con_pals_y_verbs
from codigo.vectorization import gen_vectores_ifidf
from codigo.clasificacion import gen_vector_raw

# Graficos
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix

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

# Función que obtiene los numE más representativos
def get_most_representative(ary_vt, ary_ids, ary_trm, num_e):
	# Preparar arreglo
	ary_doc_tupla = []
	ary_res1 = []
	ary_res2 = []
	ary_res3 = []
	ary_res4 = []
	# Recorrer lista de arreglos con valores IFIDF
	for valsIFIDF in ary_vt:
		# Variable
		arytupla = []
		# Recorrer numero de terminos
		for v in range(len(valsIFIDF)):
			# Recuperar valores
			va_val = valsIFIDF[v] # Valor IFIDF
			va_pid = ary_ids[v] # ID de la Palabra
			va_pal = ary_trm[v] # Palabra real
			# Agregar valores a tupla
			arytupla.append((va_val, va_pid, va_pal))
		# Ordenar tupla de Mayor a menor con base en el valor IFIDF
		arytupla.sort(reverse=True, key=itemgetter(0))
		# Agregar a arreglo de documento-tupla
		ary_doc_tupla.append(arytupla)
	# Recorrer documentos con tuplas
	for doc_tupla in ary_doc_tupla:
		# Variables
		ary_valor = []
		ary_paids = []
		ary_palab = []
		ary_vapa = []
		# Recorrer y buscar elementos designados a recuperar
		for i in range(num_e):
			# Recuperar valores de tupla en documento
			va_val, va_pid, va_pal = doc_tupla[i]
			# Agregar valores a arreglos
			ary_vapa.append((va_val, va_pal))
			ary_valor.append(va_val) # Valor IFIDF 
			ary_paids.append(va_pid) # ID de la Palabra
			ary_palab.append(va_pal) # Palabra real
		# Asignar arreglos
		ary_res4.append(ary_vapa)
		ary_res1.append(ary_valor) # IDIDF
		ary_res2.append(ary_paids) # ID Palabra
		ary_res3.append(ary_palab) # Palabra
	# Regresar valores
	return ary_res1, ary_res2, ary_res3, ary_res4

# Función para generar arreglos de palabras y autores
def gen_arreglos_palator(a_pals, a_ids, m_ators, m_pals):
	# Variables
	dicPA = {}
	# Recorrer palabras
	for i in range(len(a_pals)):
		# Recupera palabra
		pal = a_pals[i]
		# Validar y actualizar diccionario
		if pal not in dicPA:
			# Agregar palabra a diccionario
			dicPA[pal] = {}
			dicPA[pal]["Ators"] = []
			dicPA[pal]["ID"] = a_ids[i]
	# Recorrer matriz autores
	for i in range(len(m_ators)):
		# Recuperar filas
		aryA = m_ators[i]
		aryP = m_pals[i]
		# Recorrer arreglo de autores
		for j in range(len(aryA)):
			# Recupera valores
			ato = aryA[j]
			pal = aryP[j]
			# Validar Autor y Palabra
			if ato != 0 and pal != '':
				# Validar autor
				if ato not in dicPA[pal]["Ators"]:
					# Agrega autor
					dicPA[pal]["Ators"].append(ato)
	# Regresar resultado
	return dicPA

# Formatear documentos
def get_mostrepresent_by_ator(mtz_v, mtz_p, diccPA):
	# Variables
	# Arreglos
	na = []
	ni = []
	np = []
	# Diccionario
	dicAI = {}
	# Matrices
	aa = []
	mi = []
	mi2 = []
	# Recorrer filas de matriz
	for v in range(len(mtz_v)):
		# Recuperar
		ary_vals = mtz_v[v]
		ary_pals = mtz_p[v]
		# Recorrer columnas de matriz
		for i in range(len(ary_vals)):
			# Recupera y asigna valores
			valor = ary_vals[i]
			palabra = ary_pals[i]
			ary_ators = diccPA[palabra]["Ators"]
			# Recorrer lista de Autores
			for ato in ary_ators:
				# Validar diccionario
				if ato not in dicAI:
					# Iniciar diccionario
					dicAI[ato] = []
				# Agregar elementos en matriz de autores
				dicAI[ato].append(valor)
				# Agregar elementos a lista
				na.append(ato)
				ni.append(valor)
				np.append(palabra)
	# Recorrer diccionario AI
	for ator, aryvals in dicAI.items():
		# Asignar valores
		aa.append(ator)
		mi.append(aryvals)
		mi2.append([ator, aryvals])
	# Regresar resultado
	return na, ni, aa, mi, mi2, np

# Formatear documentos
def get_mostrepresent_by_pals(mtz_v, mtz_ip, mtz_sp):
	# Variables
	# Arreglos
	np = []
	ni = []
	nr = []
	# Recorrer filas de matriz
	for v in range(len(mtz_v)):
		# Recuperar
		ary_vals = mtz_v[v]
		ary_ipals = mtz_ip[v]
		ary_spals = mtz_sp[v]
		# Recorrer columnas de matriz
		for i in range(len(ary_vals)):
			# Recupera y asigna valores
			valor = ary_vals[i]
			idpal = ary_ipals[i]
			spal = ary_spals[i]
			# Agregar elementos a lista
			ni.append(valor)
			np.append(idpal)
			nr.append(spal)
	# Regresar resultado
	return np, ni, nr

# Generar Scatterplot de datos
def construirScatterPlot2D (nx, ny, lx, ly, t, a, noms):
	# Variables
	diccColors = {}
	vcolors = []
	# Recorrer eje X
	for vx in nx:
		# Validar y generar color
		if vx not in diccColors:
			diccColors[vx] = np.random.random_sample()
		# Agregar color en arreglo de colores
		vcolors.append(diccColors[vx])
	# ScatterPlot
	fig = plt.figure()
	# Asignar valor Scatter
	plt.scatter(nx, ny, c=vcolors)
	# Validar
	#if noms != None:
	#	# Recorrer 
	#	for i, nom in enumerate(noms):
	#		x = ny[i]
	#		y = ny[i]
	#		plt.text(x+0.3, y+0.3, nom, fontsize=9)
	# ScatterPlot
	plt.xlabel(lx)
	plt.ylabel(ly)
	plt.title(t)
	fig.savefig('./__graficas/' + a + '.png', dpi=300, quality=80, optimize=True, progressive=True)

# Función para generar 2 arreglos de un B resultante, con base en los autores
def get_arys_of_by_autor(bx, idators):
	# Variables
	nx = []
	ny = []
	# Recorrer B generada
	for i in range(len(bx)):
		# Recuperar valores
		aryidf = bx[i]
		idator = idators[i]
		# Recorrer valores IFIDF recuperados
		for valIF in aryidf:
			# Agregar elementos en arreglos objetivos
			nx.append(idator)
			ny.append(valIF)
	# Regresar resultado
	return nx, ny

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

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
	# X: IFIDF - Matriz
	# Y: ID Terminos - Matriz
	# Z: ID Autor - Matriz
	# W: Palabras - Matriz
	# P: Palabras - Array
	# Q: ID Palabras - Array
	# A: ID Autor - Array
	X_rw, Y_rw, Z_rw, W_rw, P_rw, Q_rw, A_rw = gen_vector_raw(listStopWords, df, X_raw, gen_vectores_ifidf, gen_dicc_con_pals_y_verbs)

	# Generar diccionario de "PALABRA" con ID y Autores
	diccPalAtors = gen_arreglos_palator(P_rw, Q_rw, Z_rw, W_rw)

	# Reducir
	svd = TruncatedSVD(n_components=100)
	svd_u = svd.fit_transform(X_rw)
	svd_vt = svd.components_

	# Obtener los 10 más representativos
	# mtz_vals - Valores IFIDF
	# mtz_idspals - ID de Palabras
	# mtz_solopals - Palbras reales
	# mtz_vip - TUPLA ValorIFIDF+PalabraReal
	mtz_vals, mtz_idspals, mtz_solopals, mtz_vip = get_most_representative(svd_vt, Q_rw, P_rw, 10)

	# Formatear arreglos
	nators, nifidf, aryatos, mtzifidf, mtzIA, npalabras = get_mostrepresent_by_ator(mtz_vals, mtz_solopals, diccPalAtors)
	construirScatterPlot2D(nators, nifidf, 'Autor', 'IFIDF', 'Las 10 palabras importantes', 'img10Palabras1', npalabras)

	# Formatear arreglos
	nidpals, nifidf, nrpal = get_mostrepresent_by_pals(mtz_vals, mtz_idspals, mtz_solopals)
	construirScatterPlot2D(nidpals, nifidf, 'Palabra', 'IFIDF', 'Las 10 palabras importantes', 'img10Palabras2', None)

	# Equivalencias
	A = np.array(X_rw)
	VT2 = np.array(svd_vt[0:2])
	VT3 = np.array(svd_vt[0:3])

	B2 = np.dot(A, VT2.transpose())
	B3 = np.dot(A, VT3.transpose())

	# Formatear arreglos
	nx, ny = get_arys_of_by_autor(B2, A_rw)
	construirScatterPlot2D(nx, ny, 'Autor', 'IFIDF', 'B2', 'imgB2', None)
	
	# Formatear arreglos
	nx, ny = get_arys_of_by_autor(B3, A_rw)
	construirScatterPlot2D(nx, ny, 'Autor', 'IFIDF', 'B3', 'imgB3', None)