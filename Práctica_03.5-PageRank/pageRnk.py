###---!/usr/bin/env python
###--- -*- coding: utf-8 -*-

# Librerias
import sys
import json
import random
import operator
import string
import unicodedata

sys.stdout.encoding
'UTF-8'

# Libreria NLTK
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize.toktok import ToktokTokenizer
from nltk.metrics.distance import edit_distance
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

# Variables
nomArch = "atexto.txt"

# Leer argumentos y recuperar nombre del archivo
if 2 <= len(sys.argv):
	# Recuperar nombre del archivo
	nomArch = str(sys.argv[1])

# Iniciar Tokenizador
toktok = ToktokTokenizer()
# Crear Tokenizar de oraciones
es_tokenizar_oraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Generar lista de palabras funcionales
list_palabrasfuns = stopwords.words("spanish")
list_puntuaciones = list(string.punctuation)
list_puntuaciones.append("¿")
list_puntuaciones.append("¡")

# Lematizador
stemmer = SnowballStemmer("spanish")

# Función de tokenización
def tokenizacion (archivo, list_palbrsfuns = None, list_puntuans = None):
	# Variables
	list_parrafos = []
	# Leer documento
	with open(archivo, 'r', encoding="utf-8") as myFile: # open(archivo, encoding="latin-1")
		# Recuperar lineas del texto
		linsArch = myFile.readlines()
		# Cerrar archivo
		myFile.close()
		# Recorrer parrafos del archivo
		for parrafo in linsArch:
			# Variables auxiliar
			list_segmentos = []
			# Rcuperar las oraciones del parrafo
			oraciones = es_tokenizar_oraciones.tokenize(parrafo)
			# Recorrer oraciones
			for sss in oraciones:
				# Generar lista de tokens
				list_tokens = toktok.tokenize(sss)
				list_tknsFinal = []
				# Validar si esta la lista de palabras funcionales
				if list_palbrsfuns != None and list_puntuans != None:
					# Recorrer tokens
					for tkn in list_tokens:
						# Token en minusculas
						tkn_lower = tkn.lower()
						# Validar si el token esta o no en la lista de palabras funciones y de puntuacion
						if tkn_lower not in list_palbrsfuns and tkn_lower not in list_puntuans:
							# Reducir la dimensalidad de los tokens
							# tkn = stemmer.stem(tkn)
							# Agregar token a lista de tokens
							list_tknsFinal.append(tkn)
				else:
					list_tknsFinal = list_tokens
				# Agregar oraciones tokenizadas a la lista de oraciones
				list_segmentos.append(list_tknsFinal)
			# Agregar el parrafo tokenizado a la lista de parrafos
			list_parrafos.append(list_segmentos)
	# Regresar lista
	return list_parrafos

# Tokenizar archivo
list_parrafos = tokenizacion (nomArch, list_palabrasfuns, list_puntuaciones)

# Función para calcular el valor PR de un nodo PageRange
def calcularPR(keyMaster, diccionario):
	# Recuperar llaves de links
	nodoPR = diccionario[keyMaster]
	backLinks = nodoPR["L"]
	# Variable PageRank
	valorPRc = 0
	# Recorrer links
	for key_link in backLinks:
		# Validar, si no es llave maestra
		if key_link != keyMaster:
			# Recuperar PageRank de un nodo en el diccionario
			valorPRoNodo = diccionario[key_link]["PR"]
			valorNmLksNd = len(diccionario[key_link]["L"])
			# Calcular valor de PageRank
			valorPRc = valorPRc + (valorPRoNodo/valorNmLksNd)
	# Validar tamaño de del valor calculado
	if valorPRc <= 0:
		# Si es 0 se asigna el peso
		valorPRc = nodoPR["PR"]
	# Regresar valor PageRank
	return valorPRc

# Función para calcular el valor y las relaciones range del texo
def pageRange (list_parrafos):
	# Variable diccionario { "Llave": { "PR": número, "L": ["Llave_1", "Llave_2", "Llave_3"] } }
	diccionario = {}
	# Recorrer parrafos
	for parrafo in list_parrafos:
		# Recorrer oraciones
		for oracion in parrafo:
			# Recorrer tokens para buscar llaves
			for token_key in oracion:
				# Validar existancia de token en el diccionario
				if token_key not in diccionario:
					# Inicializar elemento de diccionario
					diccionario[token_key] = {"PR": -1, "L": []}
				# Recorrer tokens para buscar relaciones
				for token_link in oracion:
					# Comparar Llaves y Links; y validar existencia de Link
					if token_key != token_link and token_link not in diccionario[token_key]["L"]:
						# Relacionar con la Llave
						diccionario[token_key]["L"].append(token_link)
	# Contar el número de nodos en el diccionario
	numNodes = len(diccionario)
	# Diccionario de comparación
	dicCompare = {}
	# Recorrer nodos para calcular peso
	for tknKey in diccionario.keys():
		# Se inicializa el PageRank inicial para un nodo en el diccionario
		diccionario[tknKey]["PR"] = 1
		# Inicializar diccionario de comparación con el valor del peso
		dicCompare[tknKey] = {"PR": diccionario[tknKey]["PR"]}
	# Bandera de comparación
	existenCambios = True
	# Mientras existan cambios
	while existenCambios:
		# Recorrer nodos para calcular PR
		for tknKey in diccionario.keys():
			# Calcular PR
			diccionario[tknKey]["PR"] = calcularPR(tknKey, diccionario)
		# Se considera que ya no existen cambios
		existenCambios = False
		# Comparar diccionarios
		for tknKey in diccionario.keys():
			# Comparar PRs de diccionarios
			if diccionario[tknKey]["PR"] != dicCompare[tknKey]["PR"]:
				# Indicar que aún existen cambios
				existenCambios = True
				break
		# Respaldar diccionario para su comparación
		for tknKey in diccionario.keys():
			# Resguardar valor
			dicCompare[tknKey]["PR"] = diccionario[tknKey]["PR"]
	# Regresar diccionario
	return diccionario

# Función para apoyar la organización del diccionario
def keyFuncLambda(item):
    key, subDic = item
    return subDic["PR"]

# Calcular el PR de la lista de tokens
diccionario = pageRange(list_parrafos)

# Diccionario objetivo
diccObj = {}
# Recorrer diccionario ordenado
for key, subDic in diccionario.items():
	# Llenar diccionaro obejtivo
	diccObj[key] = {"PR": subDic["PR"], "L": len(subDic["L"])}

# Ordenar diccionario
diccOrdenado = sorted(diccObj.items(), key = keyFuncLambda, reverse = True)

# Imprimir el diccionario resultante
#print ("PAGE RANK - Resultados")
#print (json.dumps(diccOrdenado, indent=3, ensure_ascii=False))

# Guardar resultados
with open('./_resultado.txt', 'w') as myFile: # open('./_resultado.txt', 'w', encoding="utf-8")
	# Finalizar texto
	myFile.write(json.dumps(diccOrdenado, indent=3, ensure_ascii=False))
	myFile.close()

# Mensaje 
print ("Tarea completada en \"_resultados.txt\"")
