#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias
import sys
import json
import random
import operator
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.metrics.distance import edit_distance
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

# Iniciar Tokenizador
toktok = ToktokTokenizer()
# Tokenizar oraciones
es_tokenizar_oraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Función de tokenización
def tokenizacion (ruta):
	# Variables
	list_tokens_gral = []
	# Leer documento
	with open(ruta, encoding="utf8") as myFile:
		# Obtener texto
		lineas = myFile.readlines()
		# Recorrer lineas
		for linea in lineas:
			# Variables
			list_tkns = []
			# Obtener oraciones de los parrafos
			oraciones = es_tokenizar_oraciones.tokenize(linea)
			# Recorrer oraciones
			for s in oraciones:
				# Agregar palabras a lista
				list_tkns.append(toktok.tokenize(s))
			# Agregar oraciones a lista general
			list_tokens_gral.append(list_tkns)
	# Regresar lista
	return list_tokens_gral

# Tokenizar archivo
lista_tokens = tokenizacion ("./Recursos/corrigeme.txt")

# Obtener lista de palabras funcionales
lista_palsfuns = stopwords.words("spanish")

# Lematizador
stemmer = SnowballStemmer("spanish")

# Función de lematización ingenua
def lematizacion_ingenue (ruta, listpalsfuns):
	# Variables
	list_lemas = {}
	# Leer documento
	with open(ruta, encoding="utf8") as myFile:
		# Obtener texto
		lineas = myFile.readlines()
		# Recorrer oraciones
		for linea in lineas:
			# Segmentar linea
			linea_segm = linea.split("\t")
			# Validar
			if len(linea_segm) > 1:
				# Limpiar [1]
				linea_sm2 = linea_segm[1].split("\n")
				linea_sm2 = linea_sm2[0]
				linea_sm1 = linea_segm[0]
				# Validar, solo agregar a lista si no es palabra funcional
				if linea_sm1 not in listpalsfuns and linea_sm2 not in listpalsfuns:
					## Evitar lemas repetidos
					if linea_sm2 not in list_lemas:
						# Agregar lemas
						list_lemas[linea_sm2] = linea_sm1
			else:
				linea_sm1 = linea_segm[0].split("\n")
				linea_sm1 = linea_sm1[0]
				linea_sm2 = stemmer.stem(linea_sm1)
				# Validar, solo agregar a lista si no es palabra funcional
				if linea_sm1 not in listpalsfuns and linea_sm2 not in listpalsfuns:
					## Evitar lemas repetidos
					if linea_sm2 not in list_lemas:
						# Agregar lemas
						list_lemas[linea_sm2] = linea_sm1

	# Regresar lista
	return list_lemas

# Función de correción ortografica
def correccion_ortografica (diccionario, list_tokens, listpalsfuns):
	# Recorrer parrafos de lista de tokens
	for x in range(len(list_tokens)):
		# Recorrer oraciones de parrafos
		for y in range(len(list_tokens[x])):
			# Recorrer palabras de oraciones
			for z in range(len(list_tokens[x][y])):
				# Palabra objetivo
				palabra = list_tokens[x][y][z]
				# Validar, solo revisar si no es palabra funcional
				if palabra not in listpalsfuns:
					# Recorrer lemas
					for key, value in diccionario.items():
						# Calcular distancia de Levenshtine
						distancia = edit_distance(palabra, key)
						# Validar distancia
						if distancia < 4:
							list_tokens[x][y][z] = value
							break
	# Regresar lista de tokens actualizada
	return list_tokens

# Lematizar
lista_lemas = lematizacion_ingenue ("./Recursos/lemmatization-es.txt", lista_palsfuns)
lista_tokens = correccion_ortografica(lista_lemas, lista_tokens, lista_palsfuns)

# Lematizar
lista_general = lematizacion_ingenue ("./Recursos/listado-general.txt", lista_palsfuns)
lista_tokens = correccion_ortografica(lista_general, lista_tokens, lista_palsfuns)

# Guardar resultados
with open('./Recursos/corregido.txt', 'w', encoding="utf-8") as myFile:
	# Texto
	nvoTexto = ""
	# Recorrer parrafos de lista de tokens
	for parrafos in lista_tokens:
		# Recorrer oraciones de parrafos
		for oraciones in parrafos:
			# Recorrer palabras de oraciones
			for palabra in oraciones:
				# Concatenar palabras
				nvoTexto = nvoTexto + " " + palabra
			# Finalizar oración
			# nvoTexto = nvoTexto + "."
		# Finalizar parrafo
		nvoTexto = nvoTexto + "\n"
	# Finalizar texto
	myFile.write(nvoTexto)