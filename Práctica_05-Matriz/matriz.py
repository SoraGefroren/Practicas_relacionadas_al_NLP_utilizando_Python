#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Librerias
import re
import sys
import json
import string
import random
import operator
import unicodedata
import math

sys.stdout.encoding
'UTF-8'

# Libreria NLTK
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

from nltk.tokenize.toktok import ToktokTokenizer
from nltk.metrics.distance import edit_distance
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

# Variables
nombreArchivo = "documentos.txt" # "docsmini.txt" # "documentos.txt"

# Stemmer en Español
stemmer = SnowballStemmer("spanish")

# Iniciar Tokenizador
toktok = ToktokTokenizer()

# Crear Tokenizar de oraciones
esTokenizarOraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Generar lista de palabras funcionales
listPalabrasfuns = stopwords.words("spanish")
listPuntuaciones = list(string.punctuation)
listPuntuaciones.append("¿")
listPuntuaciones.append("¡")

# Función para imprimir matriz
def imprimir_matriz(matriz):
	# Variable de cabecera
	strCab = "D_"
	banCab = True
	# Recorrer matriz
	for nom, fila in matriz.items():
		# Variable cadena
		imprCad = nom
		# Recorrer filas
		for key, value in fila.items():
			# Validar si crear cabecera
			if banCab:
				strCab += "\t\t\t" + key
			# Armar dadena de impresión
			imprCad += "\t\t\t" + str(value)
		# Validar si imprimir cabecera
		if banCab:
			banCab = False
			print (strCab)
		# Imprimir fila
		print (imprCad)

# Función para generar cadena CSV de matriz
def generar_csv_string_matriz(matriz):
	# Variable de cabecera
	strCSV = ""
	strCab = "D_"
	banCab = True
	# Recorrer matriz
	for nom, fila in matriz.items():
		# Variable cadena
		imprCad = nom
		# Recorrer filas
		for key, value in fila.items():
			# Validar si crear cabecera
			if banCab:
				strCab += "," + key
			# Armar dadena de impresión
			imprCad += "," + str(value)
		# Validar si imprimir cabecera
		if banCab:
			banCab = False
			strCSV += (strCab + "\n")
		# Imprimir fila
		strCSV += (imprCad + "\n")
	# Regresar cadena CSV
	return strCSV

# Función para generar cadena CSV de definiciones
def generar_csv_string_definiciones(definiciones):
	# Variable de cabecera
	strCSV = ""
	# Recorrer definiciones
	for nom, oraciones in definiciones.items():
		# Agregar nombre de fila
		strCSV += nom
		# Recorrer oraciones
		for tokens in oraciones:
			# Recorrer tokens
			for tkn in tokens:
				# Armar dadena de impresión
				strCSV += "," + tkn
		# Imprimir fila
		strCSV += "\n"
	# Regresar cadena CSV
	return strCSV

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

# Leer documento con StopWords
listStopWords = leer_stop_words("stopwords-es.txt")

# Función de tokenización
def leer_archivo_documento (archivo):
	# Variables
	documentos = {}
	definiciones = {}
	# Leer documento
	with open(archivo, 'r', encoding="utf-8") as myFile: # open(archivo, encoding="latin-1")
		# Recuperar lineas del texto
		lins_arch = myFile.readlines()
		contador = 1
		# Recorrer parrafos del archivo
		for parrafo in lins_arch:
			# Limpiar y reducir texto
			parrafo = parrafo.strip().lower()
			# Validar
			if parrafo != None and parrafo != "":
				# Tokenizar texto
				oraciones = esTokenizarOraciones.tokenize(parrafo)
				list_orasOriginal = []
				list_orasFinal = []
				# Recorrer oraciones
				for oracion in oraciones:
					# Generar lista de tokens de la oracion
					list_tokens = toktok.tokenize(oracion)
					list_tknsOriginal = []
					list_tknsFinal = []
					# Recorrer tokens
					for tkn in list_tokens:
						# Reducir palabra
						tkn = tkn.lower()
						# Validar si tomar en cuanto
						if tkn not in listPalabrasfuns and tkn not in listPuntuaciones and tkn not in listStopWords:
							# Reducir la dimensalidad del token
							tknMini = stemmer.stem(tkn)
							# Agregar token a lista de tokens
							list_tknsFinal.append(tknMini)
							# Agregar token a lista de tokens
							list_tknsOriginal.append(tkn)
					# Agregar lista de tokens a lista de oraciones
					list_orasFinal.append(list_tknsFinal)
					# Agregar lista de tokens a lista de oraciones
					list_orasOriginal.append(list_tknsOriginal)
				# Agregar oraciones a documento
				documentos["D" + str(contador)] = list_orasFinal
				definiciones["D" + str(contador)] = list_orasOriginal
				contador += 1
		# Cerrar archivo
		myFile.close()
	# Regresar json de documentos
	return documentos, definiciones

# Función de tokenización y creación de la matriz de relación termino-documento
def generar_matriz_term_doc(list_documentos):
	# Variable matriz
	matriz_dt = {}
	list_terminos = []
	# Recorrer documentos
	for nom_doc, list_oras in list_documentos.items():
		# Recorrer oraciones
		for list_tkns in list_oras:
			# Recorrer lista de tokens
			for tkn in list_tkns:
				# Validar si agregar token a lista de términos
				if tkn not in list_terminos:
					# Agregar token a lista de términos
					list_terminos.append(tkn)
	# Recorrer documentos
	for nom_doc, list_oras in list_documentos.items():
		# Validar existencia de llave
		if nom_doc not in matriz_dt:
			# Definir llave en matriz
			matriz_dt[nom_doc] = {}
			# Recorrer lista de términos
			for term in list_terminos:
				# Definir términos en matriz
				matriz_dt[nom_doc][term] = 0
		# Recorrer oraciones
		for list_tkns in list_oras:
			# Recorrer lista de tokens
			for term in list_tkns:
				# Aumentar contador de tokens
				matriz_dt[nom_doc][term] += 1
	# Devolver matriz de relación de términos - documento
	return matriz_dt

# Función para calcular el valor IT IDF y crear su matriz
def generar_matriz_it_idf (matriz_dt):
	# Calcular ITIDF
	matriz_itidf = {}
	matriz_td_v = {}
	numTotDocs = 0
	# IT
	# Recorrrer matriz
	for nom_doc, dicc_terms in matriz_dt.items():
		# Contar documento
		numTotDocs += 1
		# Variable para calcular número de términos
		numTermsInF = 0
		# AJUSTES
		# Validar si agregar documento en matriz itidf
		if nom_doc not in matriz_itidf:
			# Agregar documento en matriz itidf
			matriz_itidf[nom_doc] = {}
		# Recorrer diccionario de terminos
		for term, value in dicc_terms.items():
			# MATRIZ T-D
			# Validar si agregar término a matriz Termino-Documento
			if term not in matriz_td_v:
				# Agregar término a matriz Termino-Documento
				matriz_td_v[term] = 0
			# MATRIS IT IDF
			# Validar si agregar término a matriz itidf
			if term not in matriz_itidf[nom_doc]:
				# Agregar documento en matriz itidf
				matriz_itidf[nom_doc][term] = 0
			# Validar valor de término
			if value > 0:
				# Aumentar contador de número de términos
				numTermsInF += 1
				# Contar aparición de termino en documento
				matriz_td_v[term] += 1
		# ------------------------------------------------
		# ------------------------------------------------
		# CALCULO IT
		# Recorrer diccionario de terminos para IT
		for term, value in dicc_terms.items():
			# Validar para calculo
			if numTermsInF > 0:
				# CALCULO IT
				matriz_itidf[nom_doc][term] = value/numTermsInF
		# ------------------------------------------------
		# ------------------------------------------------
	# ITIDF
	# Recorrrer matriz
	for nom_doc, dicc_terms in matriz_itidf.items():
		# ------------------------------------------------
		# ------------------------------------------------
		# CALCULO IDF
		# Recorrer matriz IT
		for term, it_value in dicc_terms.items():
			# Valor inicial
			idf_val = 0
			# Validar si calcular ITIDF
			if matriz_td_v[term] > 0:
				# Calcular valor IDF
				idf_val = numTotDocs/matriz_td_v[term]
				idf_val = math.log(idf_val)
			# CALCULO ITIDF
			matriz_itidf[nom_doc][term] = it_value * idf_val
		# ------------------------------------------------
		# ------------------------------------------------
	# Devolver matriz ITIDF
	return matriz_itidf

# Función para calcular el producto A * B
def calcular_producto_ab (vector_a, vector_b):
	# Producto
	sumaAxB = 0
	# Recorrer vector
	for key in vector_a:
		# Calcular producto A * B
		sumaAxB += (vector_a[key] * vector_b[key])
	# Regresar la suma del producto de A * B
	return sumaAxB

# Función para calcular la magnitud de un Vector X
def calcular_magnitud (vector_x):
	# Variables y calculo de valores
	raizX = 0
	sumaXxX = calcular_producto_ab(vector_x, vector_x)
	# Validar calculo de raiz
	if sumaXxX > 0:
		raizX = math.sqrt(sumaXxX)
	# Regresar magnitud
	return raizX

# Función para calcular el coseno de dos Vectores
def calcular_coseno (vector_a, vector_b):
	# Producto
	sumaAxB = calcular_producto_ab(vector_a, vector_b)
	sumaRaizA2 = calcular_magnitud(vector_a)
	sumaRaizB2 = calcular_magnitud(vector_b)
	# Calcular cosceno
	cosenoAxB = 0
	# Validar calculo de coseno
	if sumaRaizA2 > 0 and sumaRaizB2 > 0:
		cosenoAxB = sumaAxB / (sumaRaizA2 * sumaRaizB2)
	# Regresar coseno
	return cosenoAxB

# Función para calcular la similitud de conseno de dos vectores y crear su matriz
def generar_matriz_coseno (matriz_itidf):
	# Matriz conseno
	matriz_coseno = {}
	#Recorrer matriz ITIDF, manejandolos como vectores
	for nom_vector_A, vector_terms_A in matriz_itidf.items():
		# Validar existencia de fila
		if nom_vector_A not in matriz_coseno:
			# Inicializar fila
			matriz_coseno[nom_vector_A] = {}
		#Recorrer matriz ITIDF, manejandolos como vectores
		for nom_vector_B, vector_terms_B in matriz_itidf.items():
			# Validar existencia de columna en fila
			if nom_vector_B not in matriz_coseno[nom_vector_A]:
				# Agregar columna en fila
				matriz_coseno[nom_vector_A][nom_vector_B] = calcular_coseno(vector_terms_A, vector_terms_B)			
	# Regresar Matriz de Coseno
	return matriz_coseno

# Leer archivo
listDocumentos, listDefiniciones = leer_archivo_documento(nombreArchivo)
matrizDeRelDT = generar_matriz_term_doc(listDocumentos)
matrizItIdf = generar_matriz_it_idf(matrizDeRelDT)
matrizCoseno = generar_matriz_coseno(matrizItIdf)

#imprimir_matriz(matrizDeRelDT)
#imprimir_matriz(matrizItIdf)
#imprimir_matriz(matrizCoseno)

# Generar matrices
csvDefiniciones = generar_csv_string_definiciones(listDefiniciones)
csvDeRelDT = generar_csv_string_matriz(matrizDeRelDT)
csvItIdf = generar_csv_string_matriz(matrizItIdf)
csvMCoseno = generar_csv_string_matriz(matrizCoseno)
csvStrFile = csvDefiniciones + u"\n\n" + csvDeRelDT + u"\n\n" + csvItIdf + u"\n\n" + csvMCoseno

# Guardar resultados
with open('matriz-coseno.csv', 'w', encoding="utf-8") as myFile:
	# Grabar diccionario ordenado en archivo de texto
	myFile.write(csvStrFile.encode("utf-8").decode("utf-8"))
	myFile.close()