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
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# -----------------------
# -----------------------
# 2.1. Tokenización
# Iniciar Tokenizador
toktok = ToktokTokenizer()
# Tokenizar oraciones
es_tokenizar_oraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Crear función de tokenización que reciba la ruta de un archivo y regrese una lista de tokens.
def tokenizacion (ruta):
	# Variables
	list_tokens = []
	# Leer documento
	with open(ruta, encoding="utf-8") as myFile:
		# Obtener texto
		texto = myFile.read()
		# Obtener oraciones de los parrafos
		oraciones = es_tokenizar_oraciones.tokenize(texto)
		# Recorrer oraciones
		for s in oraciones:
			list_tokens.append(toktok.tokenize(s))
	# Regresar lista
	return list_tokens

# -----------------------
# -----------------------
# 2.2 Distribución de Frecuencias
# Tokenizar archivo
lista_tokens = tokenizacion ('./Recursos/corregido.txt')

diccionario_palabras = {}
# Recorrer oraciones
for lista_palabras in lista_tokens:
	# Variable de control
	lista_pals_chec = []
	# Recorrer lista de palabras
	for palabra in lista_palabras:
		# Validar existencia de contador
		if palabra not in diccionario_palabras:
			diccionario_palabras[palabra] = 0
		# Validar existencia de palabra revisada
		if palabra not in lista_pals_chec:
			# Contar frecuencia
			diccionario_palabras[palabra] += lista_palabras.count(palabra)
			lista_pals_chec.append(palabra)
# Ordenar diccionario
dicPalsOrdenado = sorted(diccionario_palabras.items(), key=operator.itemgetter(1), reverse=True)

# Imprimir las frecuencias en orden decreciente en pantalla (usen el método sort o la función sorted).
print ("FRECUENCIA - Sin cambios: ")
print (json.dumps(dicPalsOrdenado, indent=2))

# -----------------------
# -----------------------
# 2.3 Reducción de dimensionalidad
# Obtener lista de palabras funcionales
lista_palabras_funcionales = stopwords.words("spanish")
# Usar NLTK para remover las palabras funcionales de la tokenización del archivo
# Recorrer oraciones
for i in range(len(lista_tokens)):
	# Recorrer lista da palabras funcionales
	for pFal in lista_palabras_funcionales:
		# Validar existencia de palabra funcional
		if pFal in lista_tokens[i]:
			# Remover palabra funcional
			lista_tokens[i].remove(pFal)

# Imprimir resultado
# print ("REDUCCIÓN-DIMENCIONALIDAD: ")
# print (json.dumps(lista_tokens, indent=2))

# -----------------------
# -----------------------
# 2.3.1 Distribución de Frecuencias con Stemming
# Stemmer en Español
stemmer = SnowballStemmer("spanish")
# Variable para lista de tokens con Stem
lista_tokens_stem = []
# Recorrer oraciones de lista de tokens
for i in range(len(lista_tokens)):
	lista_tokens_stem.append([])
	# Recorrer palabras
	for palabra in lista_tokens[i]:
		# Stemming con NLTK
		lista_tokens_stem[i].append(stemmer.stem(palabra))

# Lista de palabras con frecuencia
diccionario_palabras_stem = {}
# Recorrer oraciones
for lista_palabras in lista_tokens_stem:
	# Variable de control
	lista_pals_chec = []
	# Recorrer lista de palabras
	for palabra in lista_palabras:
		# Validar existencia de contador
		if palabra not in diccionario_palabras_stem:
			diccionario_palabras_stem[palabra] = 0
		# Validar existencia de palabra revisada
		if palabra not in lista_pals_chec:
			# Contar frecuencia
			diccionario_palabras_stem[palabra] += lista_palabras.count(palabra)
			lista_pals_chec.append(palabra)
# Ordenar diccionario
dicPalsOrdenado_stem = sorted(diccionario_palabras_stem.items(), key=operator.itemgetter(1), reverse=True)

# Imprimir las frecuencias en orden decreciente en pantalla (usen el método sort o la función sorted).
print ("FRECUENCIA - Con stemming: ")
print (json.dumps(dicPalsOrdenado_stem, indent=2))

# -----------------------
# -----------------------
# 2.4.Distribución de Frecuencias con Lematización ingenua
# Crear una función de lematización ingenua usando el archivo “lemmatization-es.txt”, el cual contiene un conjunto de palabras con sus respectivos lemas.
def lematizacion_ingenue (ruta):
	# Variables
	list_lemas = {}
	# Leer documento
	with open(ruta, encoding="utf-8") as myFile:
		# Obtener texto
		lineas = myFile.readlines()
		# Recorrer oraciones
		for linea in lineas:
			# Segmentar linea
			linea_segm = linea.split("\t")
			# Validar
			if len(linea_segm) > 1:
				# Limpiar [1]
				linea_segm_1 = linea_segm[1].split("\n")
				linea_segm_1 = linea_segm_1[0]
				# Validar
				if linea_segm_1 not in list_lemas:
					# Agregar lemas
					list_lemas[linea_segm_1] = linea_segm[0]
	# Regresar lista
	return list_lemas

# Lematizar
lista_lemas = lematizacion_ingenue ("./Recursos/lemmatization-es.txt")
lista_lemas_sinPF = {}
# Recorrer oraciones
for key, value in lista_lemas.items():
	# Validar existencia de palabra funcional
	if key not in lista_palabras_funcionales and value not in lista_palabras_funcionales:
		# Agregar a lista ya que no es palabra funcional
		lista_lemas_sinPF[key] = value

# Variable para lista de tokens con Stem
lista_tokens_cl = []
# Recorrer oraciones de lista de tokens
for i in range(len(lista_tokens)):
	lista_tokens_cl.append([])
	# Recorrer palabras
	for palabra in lista_tokens[i]:
		# Lemarizar
		for key, value in lista_lemas_sinPF.items():
			# Validar
			if palabra == key or palabra == value:
				# Stemming con NLTK
				lista_tokens_cl[i].append(stemmer.stem(value))
				break

# Lista de palabras con frecuencia
diccionario_lemas = {}
# Recorrer oraciones
for lista_palabras in lista_tokens_cl:
	# Variable de control
	lista_pals_chec = []
	# Recorrer lista de palabras
	for palabra in lista_palabras:
		# Validar existencia de contador
		if palabra not in diccionario_lemas:
			diccionario_lemas[palabra] = 0
		# Validar existencia de palabra revisada
		if palabra not in lista_pals_chec:
			# Contar frecuencia
			diccionario_lemas[palabra] += lista_palabras.count(palabra)
			lista_pals_chec.append(palabra)
# Ordenar diccionario
dicLemasOrdenado = sorted(diccionario_lemas.items(), key=operator.itemgetter(1), reverse=True)

# Imprimir las frecuencias en orden decreciente en pantalla (usen el método sort o la función sorted).
print ("FRECUENCIA - Con lematización:")
print (json.dumps(dicLemasOrdenado, indent=2))
