#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias
import sys
import random

# Funciones
def hamming (c1, c2):
	# Variables
	contador = 0
	# Validar tamaño de cadena
	if len(c1) == len(c2):
		# Recorrer cadenas
		for i in range(len(c1)):
			# Comparar cadenas
			if c1[i] != c2[i]:
				# Contar distancia
				contador += 1
	# Devolver distancia
	return contador

# Leer argumentos
if 2 < len(sys.argv):
	# Cadena 1
	cad1 = str(sys.argv[1])
	# Cadena 2
	cad2 = str(sys.argv[2])
	# Imprimir distancia
	print ("Distancia: " + str(hamming(cad1, cad2)))
