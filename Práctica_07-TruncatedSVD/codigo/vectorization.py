# Librerias
import math
import string

# Libreria NLTK
import nltk

from nltk.tokenize.toktok import ToktokTokenizer
from nltk.metrics.distance import edit_distance

# Iniciar Tokenizador
toktok = ToktokTokenizer()

# Crear Tokenizar de oraciones
esTokenizarOraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Librerias
import numpy as np
import pandas as pd

# Función de vectorización
def vectorizer(raw_text, dicc_ppa, ary_terms, autor, indice):
	# Variables
	aryR = []
	aryTest = []
	# Inicializar arreglo en cero
	for term in ary_terms:
		aryR.append(0)
	# Recuperar parrafo objetivo por indice
	parrafo = raw_text.iloc[indice]
	# Tokenizar parrafo en segmentos
	segmentos = esTokenizarOraciones.tokenize(parrafo)
	# Recorrer segmentos
	for minseg in segmentos:
		# Generar lista de tokens
		listkns = toktok.tokenize(minseg)
		# Recorrer tokens
		for tkn in listkns:
			# Si el token pertenece al arreglo de terminos
			if tkn in ary_terms and tkn not in aryTest:
				# Recupera indice de token actual
				index_t = ary_terms.index(tkn)
				# Sumar para avisar aparición de token actual
				# aryR[index_t] = aryR[index_t] + 1
				# Agregar token an AryTest
				aryTest.append(tkn)
				# Recupera número de términos en fila
				numTrmEnF = len(dicc_ppa[autor])
				# Validar calculo IT para {autor {term1: n, term2: n}}
				if numTrmEnF > 0:
					# Calcular recupera suma de valores
					aryR[index_t] = dicc_ppa[autor][tkn]/numTrmEnF
				# Valida calculo IDF para {autor {term1: n, term2: n}}
				if aryR[index_t] > 0:
					# Cuenta el número de documentos
					numDocs = len(dicc_ppa)
					# Contar repeticiones de token verticalmente
					numRepV = 0
					for temp_ator, temp_dicc_tks in dicc_ppa.items():
						if tkn in temp_dicc_tks:
							numRepV += 1
					# Re-Valida calculo IDF
					if numRepV > 0:
						# Calculas IDF
						aryR[index_t] = aryR[index_t] * math.log(numDocs/numRepV)
						# Ajuste para ver el valor y que no solo se impriman ceros
						aryR[index_t] = aryR[index_t] * 100
				
	# Generar arreglo Numpy
	npAry = np.array(aryR)
	# Retorno de arreglo
	return npAry

# Función que genera el Arreglo X y Y
def gen_vectores_ifidf (raw_text, dicc_ppa, ary_terms, autor, indice, dic_ators, dic_trms, contadorAry):
	# Variables
	aryR = []
	aryR_Y = []
	aryR_Z = []
	aryR_W = []
	aryTest = []
	# Inicializar arreglo en cero
	for term in ary_terms:
		aryR.append(0)
		aryR_Y.append(0)
		aryR_Z.append(0)
		aryR_W.append('')
	# Recuperar parrafo objetivo por indice
	parrafo = raw_text.iloc[indice]
	# Tokenizar parrafo en segmentos
	segmentos = esTokenizarOraciones.tokenize(parrafo)
	# Recorrer segmentos
	for minseg in segmentos:
		# Generar lista de tokens
		listkns = toktok.tokenize(minseg)
		# Recorrer tokens
		for tkn in listkns:
			# Si el token pertenece al arreglo de terminos
			if tkn in ary_terms and tkn not in aryTest:
				# Recupera indice de token actual
				index_t = ary_terms.index(tkn)
				# Sumar para avisar aparición de token actual
				# aryR[index_t] = aryR[index_t] + 1
				# Agregar token an AryTest
				aryTest.append(tkn)
				# Agregar
				if tkn not in dic_trms:
					# Nombrar token
					dic_trms[tkn] = contadorAry
					contadorAry += 1
				# Asignar ID
				aryR_W[index_t] = tkn
				aryR_Y[index_t] = dic_trms[tkn]
				aryR_Z[index_t] = dic_ators[autor]
				# Recupera número de términos en fila
				numTrmEnF = len(dicc_ppa[autor])
				# Validar calculo IT para {autor {term1: n, term2: n}}
				if numTrmEnF > 0:
					# Calcular recupera suma de valores
					aryR[index_t] = dicc_ppa[autor][tkn]/numTrmEnF
				# Valida calculo IDF para {autor {term1: n, term2: n}}
				if aryR[index_t] > 0:
					# Cuenta el número de documentos
					numDocs = len(dicc_ppa)
					# Contar repeticiones de token verticalmente
					numRepV = 0
					for temp_ator, temp_dicc_tks in dicc_ppa.items():
						if tkn in temp_dicc_tks:
							numRepV += 1
					# Re-Valida calculo IDF
					if numRepV > 0:
						# Calculas IDF
						aryR[index_t] = aryR[index_t] * math.log(numDocs/numRepV)
	# Generar arreglo Numpy
	npAry = np.array(aryR)
	npAry2 = np.array(aryR_Y)
	npAry3 = np.array(aryR_Z)
	npAry4 = np.array(aryR_W)
	# Retorno de arreglo
	return npAry, npAry2, npAry3, npAry4, dic_trms, contadorAry

# Función que genera el Arreglo X y Y
def gen_vectores_xy (raw_text, dicc_ppa, ary_terms, autor, indice, dic_ators, dic_trms, contadorAry):
	# Variables
	aryR = []
	aryR_Y = []
	aryR_Z = []
	aryR_W = []
	aryTest = []
	# Inicializar arreglo en cero
	for term in ary_terms:
		aryR.append(0)
		aryR_Y.append(0)
		aryR_Z.append(0)
		aryR_W.append(0)
	# Recuperar parrafo objetivo por indice
	parrafo = raw_text.iloc[indice]
	# Tokenizar parrafo en segmentos
	segmentos = esTokenizarOraciones.tokenize(parrafo)
	# Recorrer segmentos
	for minseg in segmentos:
		# Generar lista de tokens
		listkns = toktok.tokenize(minseg)
		# Recorrer tokens
		for tkn in listkns:
			# Si el token pertenece al arreglo de terminos
			if tkn in ary_terms and tkn not in aryTest:
				# Recupera indice de token actual
				index_t = ary_terms.index(tkn)
				# Sumar para avisar aparición de token actual
				# aryR[index_t] = aryR[index_t] + 1
				# Agregar token an AryTest
				aryTest.append(tkn)
				# Agregar
				if tkn not in dic_trms:
					# Nombrar token
					dic_trms[tkn] = contadorAry
					contadorAry += 1
				# Asignar ID
				aryR_Y[index_t] = dic_trms[tkn]
				aryR_Z[index_t] = dic_ators[autor]
				# Recupera número de términos en fila
				numTrmEnF = len(dicc_ppa[autor])
				# Validar calculo IT para {autor {term1: n, term2: n}}
				if numTrmEnF > 0:
					# Calcular recupera suma de valores
					aryR[index_t] = dicc_ppa[autor][tkn]/numTrmEnF
				# Valida calculo IDF para {autor {term1: n, term2: n}}
				if aryR[index_t] > 0:
					# Cuenta el número de documentos
					numDocs = len(dicc_ppa)
					# Contar repeticiones de token verticalmente
					numRepV = 0
					for temp_ator, temp_dicc_tks in dicc_ppa.items():
						if tkn in temp_dicc_tks:
							numRepV += 1
					# Re-Valida calculo IDF
					if numRepV > 0:
						# Calculas IDF
						aryR[index_t] = aryR[index_t] * math.log(numDocs/numRepV)
						# Ajuste para ver el valor y que no solo se impriman ceros
						aryR[index_t] = aryR[index_t] * 100
				
	# Generar arreglo Numpy
	npAry = np.array(aryR)
	npAry2 = np.array(aryR_Y)
	npAry3 = np.array(aryR_Z)
	npAry4 = np.array(aryR_W)
	# Retorno de arreglo
	return npAry, npAry2, npAry3, npAry4, dic_trms, contadorAry