# Librerias
import sys, os
import numpy as np
import pandas as pd

# Librerias
from codigo.analisis import gen_dicc_con_pals_y_verbs
from codigo.vectorization import vectorizer
from codigo.clasificacion import predictor_test
from codigo.clasificacion import clasifi_raw
from codigo.metrics import precision

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

# Iniciar
if __name__ == "__main__":
	# Leer documento con StopWords
	listStopWords = leer_stop_words("./docs/stopwords-es.txt")

	# Documento # _m _all
	df = pd.read_csv('./docs/author_corpus_all.txt',
		sep = '\t',
		index_col = False,
		names = ["autor","texto"])

	# Remueve autor 5, que es igual al 4
	df = df[:][df['autor'] != 5]

	# Abstraer solo los parrafos
	X_raw = df['texto']

	# Generar pred y test
	y_t, y_f, y_pLR, y_pKNN, y_pSVN = predictor_test(listStopWords, df, X_raw, vectorizer, gen_dicc_con_pals_y_verbs)
	# Imprimir resultados
	print('\n')
	print('--------------------------------')
	print('\t* BaseLine: {0}'.format(precision(y_t, y_f)))
	print('LR.')
	print('\t* Precisión: {0}'.format(precision(y_pLR, y_t)))
	print('--------------------------------')
	print('KNN.')
	print('\t* Precisión: {0}'.format(precision(y_pKNN, y_t)))
	print('--------------------------------')
	print('SVN.')
	print('\t* Precisión: {0}'.format(precision(y_pSVN, y_t)))
	# Ajuste
	#nyp = sorted(y_p, reverse=True)
	#nyt = sorted(ytrain, reverse=True)[:len(y_t)]
	#print('BaseLine: {0}'.format(precision(nyp, nyt)))