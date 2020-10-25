#---!/usr/bin/env python
#--- -*- coding: utf-8 -*-

# Librerias
import re
import sys
import json
import string
import random
import operator
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

# Libreria para Grafo
import matplotlib.pyplot as plt
import networkx as nx
import random

# Variables
miniparams = []
parametros = []
nombreArchivo = "wikipedia_es_abstracts.txt" # "OWesA.txt"

# Stemmer en Español
stemmer = SnowballStemmer("spanish")

# Recorrer parametros
for i in range(len(sys.argv)):
	# Validar
	if 0 < i:
		# Recuperar paramtros
		parm = str(sys.argv[i].strip().lower())
		# Validar asignación
		if parm not in parametros:
			# Asignar parametro
			parametros.append(parm)
			miniparams.append(stemmer.stem(parm))

# Iniciar Tokenizador
toktok = ToktokTokenizer()
# Crear Tokenizar de oraciones
esTokenizarOraciones = nltk.data.load("tokenizers/punkt/spanish.pickle")

# Generar lista de palabras funcionales
listPalabrasfuns = stopwords.words("spanish")
listPuntuaciones = list(string.punctuation)
listPuntuaciones.append("¿")
listPuntuaciones.append("¡")
listPuntuaciones.append("ja")
listPuntuaciones.append("yme")
listPuntuaciones.append("yczna")
listPuntuaciones.append("así")

# Función de tokenización
def leer_archivo (archivo, params):
	# Variables
	documento = {}
	# Leer documento
	with open(archivo, 'r', encoding="utf-8") as myFile: # open(archivo, encoding="latin-1")
		# Recuperar lineas del texto
		lins_arch = myFile.readlines()
		list_temp_parr = []
		contador = 0
		# Recorrer parrafos del archivo
		for parrafo in lins_arch:
			# Dividir por \t
			list_segmentos = parrafo.split("\t")
			# Validar tamaño
			if 2 <= len(list_segmentos):
				# Variable
				textoObjetivo = ""
				# Titulo divido por :
				list_titulo = list_segmentos[0].split(":")
				titulo = ""
				# Validar titulo
				if 2 <= len(list_titulo):
					titulo = list_titulo[1].lower()
				# Titulo divido por \n
				list_parrafo = list_segmentos[1].split("\n")
				# Validar parrafo
				textoObjetivo = ""
				if 1 <= len(list_parrafo):
					textoObjetivo = list_parrafo[0].lower()
				# Validar asginación de parrafo
				bandera = False
				for prm in params:
					if textoObjetivo.find(prm) >= 0:
						bandera = True
				# Validar asignación de parrafo
				if bandera and textoObjetivo not in list_temp_parr:
					# Agregar el parrafo a la variable documento
					documento[contador] = { "T": titulo, "P": textoObjetivo}
					list_temp_parr.append(textoObjetivo)
					contador = contador + 1
		# Cerrar archivo
		myFile.close()
	# Regresar json de documentos
	return documento

# Leer archivo
listParrafos = leer_archivo(nombreArchivo, miniparams)

# Función para buscar palabras objetivo conforme un patron
def buscar_coincidencias(list_pals_funs, list_punts, texto, one_pos, final_star_pos, expresion, dicc_de_rel = None):
	# Validar existencia de diccionario
	if dicc_de_rel == None:
		dicc_de_rel = {}
	# Crear patron
	patron_exp = re.compile(expresion)
	# Buscar coincidencias del patron en el texto
	list_matches = patron_exp.findall(texto)
	# Recorrer maches
	for mi_match in list_matches:
		# Lista de palabras de interes temporal
		list_of_temp_words = []
		# Recorrer palabras de match
		for temp_i in range(len(mi_match)):
			# Validar match
			if (temp_i == one_pos) or (temp_i >= final_star_pos):
				# Recuperar palabra relacionada
				temp_word = mi_match[temp_i]
				temp_word = re.sub(', ', '', temp_word)
				temp_word = re.sub('y ', '', temp_word)
				temp_word = temp_word.strip()
				# Validar resguardo
				if temp_word != '' and temp_word not in list_pals_funs and temp_word not in list_punts and temp_word not in list_of_temp_words:
					# Resguardar palabra relacionada
					list_of_temp_words.append(temp_word)
		if len(list_of_temp_words) > 1:
			# Recorrer palabras temporales
			my_temp_w = list_of_temp_words[0]
			# Validar existencia de parametro en diccionario
			if my_temp_w not in dicc_de_rel:
				# Lista de palabras de interes temporal
				dicc_de_rel[my_temp_w] = []
			# SubRecorrido de palabras temporales
			for m_sbtmp_w in list_of_temp_words:
				# Validar existencia en diccionario
				if m_sbtmp_w not in dicc_de_rel[my_temp_w]:
					# Guardar palabra temporal
					dicc_de_rel[my_temp_w].append(m_sbtmp_w)
	# Regresar resultados
	return dicc_de_rel

# Variable diccionario de relaciones
diccDeRel = {}

# Recorrer parrafos en diccionario
for key,value in listParrafos.items():
	# Revisar patrones y actualizar diccionario
	diccDeRel = buscar_coincidencias(listPalabrasfuns, listPuntuaciones, value["P"], 1, 3, '(las|la|los|el)*(\s*\w+) (son un|son una|es un|es una|fueron un|fueron una|fue un|fue una){1} (\w+)', diccDeRel)
	diccDeRel = buscar_coincidencias(listPalabrasfuns, listPuntuaciones, value["P"], 0, 2, '(\w+) (tal como|así tambien|así como|como por|por ejemplo|tambien conocida como|tambien conocido como|tal como:|como:|como){1} (\w+)*(,\s*\w+)*(\s*y\s*\w+)*', diccDeRel)
	diccDeRel = buscar_coincidencias(listPalabrasfuns, listPuntuaciones, value["P"], 0, 4, '(\w+) (es|forma|forman|son){1} (parte){1} (del|de las|de los|de el|de una|de un|de){1} (\w+)', diccDeRel)
	diccDeRel = buscar_coincidencias(listPalabrasfuns, listPuntuaciones, value["P"], 0, 5, '(\w+)(\s*le|\s*es|\s*son)* (perteneciente(s)*|pertenecen|pertenece|a){1} (la|al|a)* (\w+)', diccDeRel)
	diccDeRel = buscar_coincidencias(listPalabrasfuns, listPuntuaciones, value["P"], 0, 1, '(\w+)(,\s*\w+)*(\s*y\s*\w+)', diccDeRel)

# Variables
list_nodos = []
list_aristas = []

# Recorrer diccionario de relaciones
for key,arry in diccDeRel.items():
	# Validar si agregar nodo
	if key not in list_nodos:
		# Agregar nodo
		list_nodos.append(key)
	# Recorrer relaciones de la llave
	for value in arry:
		# Generar tupla
		tempTupla = (key, value)
		# Validar si agregar tupla
		if tempTupla not in list_aristas:
			# Agregar nodo
			list_aristas.append(tempTupla)
		# Validar si agregar nodo
		if value not in list_nodos:
			# Agregar nodo
			list_nodos.append(value)

# Crea grafica
Grafico = nx.DiGraph()

# Vertices
Grafico.add_nodes_from(list_nodos)

# Aristas
Grafico.add_edges_from(list_aristas)

posicion = nx.spring_layout(Grafico)
nx.draw_networkx_labels(Grafico, posicion, labels=dict([(nodo, nodo) for nodo in list_nodos]))

# Dibuja la gráfica
nx.draw(Grafico, posicion)

# Muestra en pantalla lo dibujado
plt.show()
