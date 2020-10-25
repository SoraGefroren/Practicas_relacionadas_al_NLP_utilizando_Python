# Librerias
import numpy as np
import pandas as pd

import random

# Libreria NLTK
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.metrics.distance import edit_distance
from nltk.corpus import stopwords

# Librerias
import string

# Iniciar Tokenizador
toktok = ToktokTokenizer()

# Crear Tokenizar de oraciones
esTokenizarOraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Generar lista de palabras funcionales
list_palabrasfuns = stopwords.words("spanish")
list_puntuaciones = list(string.punctuation)
list_puntuaciones.append("¿")
list_puntuaciones.append("¡")

# Generar lista de palabras funcionales
list_palabrasfuns = stopwords.words("spanish")

# Función que generar un diccionario con términos unicos por parrafo
def gen_dicc_con_pals_y_verbs (list_stopwords, x_raw):
	# Preparar variables diccionario
	dicc_global_termator = {}
	dicc_global_atorterm = {}
	lista_trmns = []
	contID_Ator = 1
	# Recorrer arreglo objetivo
	for i in range(len(x_raw)):
		# Recuperar parrafo y autor
		t_autor = x_raw["autor"].iloc[i]
		t_texto = x_raw["texto"].iloc[i]
		# Tokenizar texto en segmentos
		segmentos = esTokenizarOraciones.tokenize(t_texto)
		# Recorrer segmentos
		for minseg in segmentos:
			# Generar lista de tokens
			listkns = toktok.tokenize(minseg)
			# Recorrer tokens
			for tkn in listkns:
				# Validar validez de termino de estudio
				if tkn not in list_puntuaciones and tkn not in list_palabrasfuns and tkn not in list_stopwords:
					# -------
					# Objeto Termino-Autor
					# Inicializar token en diccionario objetivo
					if tkn not in dicc_global_termator:
						dicc_global_termator[tkn] = {}
					# Inicializar autor en diccionario objetivo
					if t_autor not in dicc_global_termator[tkn]:
						dicc_global_termator[tkn][t_autor] = 1
					else:
						# Incrementar relación autor-token en diccionario objetivo
						dicc_global_termator[tkn][t_autor] += 1
					# -------
					# Objeto Autor-Termino
					# Inicializar token en diccionario objetivo
					if t_autor not in dicc_global_atorterm:
						dicc_global_atorterm[t_autor] = {}
					# Inicializar autor en diccionario objetivo
					if tkn not in dicc_global_atorterm[t_autor]:
						dicc_global_atorterm[t_autor][tkn] = 1
					else:
						# Incrementar relación autor-token en diccionario objetivo
						dicc_global_atorterm[t_autor][tkn] += 1
					# -------
					# Agregar término a lista de terminos
					if tkn not in lista_trmns:
						lista_trmns.append(tkn)
	# Regresar resultados
	return dicc_global_atorterm, dicc_global_termator, lista_trmns