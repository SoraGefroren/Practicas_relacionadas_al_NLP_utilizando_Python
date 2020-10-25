#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias
import sys
import json
import random

_stdin_encoding = sys.stdin.encoding or 'utf-8'

# Clase "Agente"
class Agente:
	# Constructor
	def __init__(self, _id):
		self._id = _id
		self.inventario = {}
	
	# Generar nombre aleatorio
	def nombrar(self):
		# Variables
		nombre = ""
		nSilabas = random.randint(1, 8)
		listV = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
		listC = ["a", "e", "i", "o", "u"]
		# Armar palabra
		for i in range(nSilabas):
			v = random.choice(listV)
			c = random.choice(listC)
			nombre  = nombre + v + c
		# Devolver nombre
		return nombre
	# Método que busca un objeto en el inventario y devuelve el nombre encontrado más chico
	def buscarNombreDe(self, objeto):
		# Variables
		nombre = None
		# Buscar objeto en lista inventario
		if 0 < len(self.inventario):
			for key, value in self.inventario.items():
				# Comparar llave y objeto
				if key == objeto:
					# Recuperar lista de nombres
					listNoms = value
					nombre = ""
					# Comparar nombres de lista
					for name in listNoms:
						if len(name) < len(nombre) or (not nombre or nombre == ""):
							nombre = name
					break
		# Devolver nombre
		return nombre
	# Método que busca un objeto en el inventario y devuelve a lista de nombres encontrados
	def buscarNombresDe(self, objeto):
		# Variables
		listNoms = None
		# Buscar objeto en lista inventario
		if 0 < len(self.inventario):
			for key, value in self.inventario.items():
				# Comparar llave y objeto
				if key == objeto:
					listNoms = value
					break
		# Devolver lista
		return listNoms
	# Método para agregar un objeto a la correspondiente lista de nombre del inventario
	def agregarEnInventario(self, objeto, nombre):
		# Variable
		existeLista = False
		# Buscar objeto en lista inventario
		if 0 < len(self.inventario):
			for key, value in self.inventario.items():
				# Comparar llave y objeto
				if key == objeto:
					# Ver existencia de nombre en lista
					if nombre not in self.inventario[key]:
						# Agregar nombre a inventario
						self.inventario[key].append(nombre)
					# Cambiar valor de bandera
					existeLista = True
					break
		# Ver existencia de lista
		if not existeLista:
			# Agregar objeto y nombre a inventario
			self.inventario[objeto] = [nombre]
	# Método para reiniriciar el inventario con el nombre dado como unico valor en lista
	def reiniciarEnInventarioCon(self, objeto, nombre):
		# Buscar objeto en lista inventario
		if 0 < len(self.inventario):
			for key, value in self.inventario.items():
				# Comparar llave y objeto
				if key == objeto:
					# Agregar nombre a inventario
					self.inventario[key] = [nombre]
					break
	# Método de comunicación
	def enunciar(self, objeto, oyente):
		# El proceso fallo?
		isOk = False
		# Recuperar nombre del hablante
		nomHablante = self.buscarNombreDe(objeto)
		# Recuperar lista de nombres del oyente
		# 2. El oyente escucha y busca si el nombre esta en su inventario, para el mismo objeto.
		listNomsOyente = oyente.buscarNombresDe(objeto)
		# Si no exiten nombre conocido para el objeto, este se inventa
		if (not nomHablante or nomHablante == "" or nomHablante == None) and (not listNomsOyente or listNomsOyente == None or len(listNomsOyente) == 0):
			# Generar nombres aleatorios
			# 1. Si no tiene un nombre para ese objeto, lo inventa.
			nombreH = self.nombrar()
			# Se agregan al inventario los nombres inventados
			# 4. Si el oyente no tiene ese nombre para el objeto en su inventario, el actualiza su inventario añadiendo el nombre que escucho
			self.agregarEnInventario(objeto, nombreH)
			oyente.agregarEnInventario(objeto, nombreH)
		else:
			if (not nomHablante or nomHablante == "" or nomHablante == None):
				# Generar nombres aleatorios
				# 1. Si no tiene un nombre para ese objeto, lo inventa.
				nombreH = self.nombrar()
				# Se agregan al inventario los nombres inventados
				# 4. Si el oyente no tiene ese nombre para el objeto en su inventario, el actualiza su inventario añadiendo el nombre que escucho
				self.agregarEnInventario(objeto, nombreH)
				oyente.agregarEnInventario(objeto, nombreH)
			else:
				if (not listNomsOyente or listNomsOyente == None or len(listNomsOyente) == 0):
					# El oyente agrega el nombre a su inventario
					# 4. Si el oyente no tiene ese nombre para el objeto en su inventario, el actualiza su inventario añadiendo el nombre que escucho
					oyente.agregarEnInventario(objeto, nomHablante)
				else:
					# Bandera para saber localización de nombre
					nombreEncontrado = False
					# Buscar objeto en lista inventario
					for nomsDeOy in listNomsOyente:
						# Comparar llave y objeto
						if nomsDeOy == nomHablante:
							# 3. En este de que los nombres sean iguales, ambos agentes descartan cualquier otro nombre que tengan para ese objeto y se quedan con el que fue enunciado
							# Se reinicia lists de nombres en inventario
							self.reiniciarEnInventarioCon(objeto, nomHablante)
							oyente.reiniciarEnInventarioCon(objeto, nomHablante)
							# Recuperar lista de nombre del hablante
							nombreEncontrado = True
							# 3. Si el oyente tiene el mismo nombre para el objeto, la interacción es un exito.
							isOk = True
							break
					# Si el oyente no conoce el nombre
					if not nombreEncontrado:
						# El oyente agrega el nombre a su inventario
						# 4. Si el oyente no tiene ese nombre para el objeto en su inventario, el actualiza su inventario añadiendo el nombre que escucho
						oyente.agregarEnInventario(objeto, nomHablante)
		# Si el proceso fallo?
		return isOk
	# Método para imprir el estadode agente
	def imprimirEstado(self):
		# Imprimir inventario del agente
		print ("\t- Agente \"" + str(self._id) + "\"")
		print ("```json")
		print json.dumps(self.inventario, indent=4)
		print ("```")

# Leer argumentos
if 3 < len(sys.argv):
	# Número de agentes
	n = int(sys.argv[1])
	# Número de objetos
	m = int(sys.argv[2])
	# Número de iteraciones
	max_i = int(sys.argv[3])
	# Variables
	agenteX = Agente(-1)
	listAgentes = []
	listObjetos = []
	# Crear agente
	for i in range(n):
		listAgentes.append(Agente(i))
	# Crear objetos
	for i in range(m):
		newName = agenteX.nombrar()
		listObjetos.append(newName)
	# Realizar iteraciones
	for i in range(max_i):
		# Inicia iteración
		print (u"***Iteración \"" + str(i).decode(_stdin_encoding) + u"\"***")
		# seleccionar posicipon del hablador
		posH = random.randint(0, (n - 1))
		posO = random.randint(0, (n - 1))
		# Enunciar
		print (u"1. Resultado de enunciar")
		# Validar posición de oyente
		while posH == posO:
			posO = random.randint(0, (n - 1))
		# --------------------------------------
		# CODIGO ANTERIOR ----------------------
		# Recorrer objetos
		# for obj in listObjetos:
			# iteración
			# if listAgentes[posH].enunciar(obj, listAgentes[posO]):
				# print (u"\t- [Termina revisión de objeto \"" + str(obj).decode(_stdin_encoding) + u"\": Exito]")
			# else:
				# print (u"\t- [Termina revisión de objeto \"" + str(obj).decode(_stdin_encoding) + u"\": Fallo]")
    	# --------------------------------------
     	# --------------------------------------
		# --------------------------------------
		# CODIGO NUEVO -------------------------
		# 1. Se elige un objeto y el hablante enuncia el nombre que conoce del mismo.
		# Seleccionar objeto aleatorio
  		pObj = random.randint(0, (m - 1))
		strObj = listObjetos[pObj]
		# Enunciar a Oyente
		if listAgentes[posH].enunciar(strObj, listAgentes[posO]):
			# 3. Si el oyente tiene el mismo nombre para el objeto, la interacción es un exito.
			print (u"\t- [Termina revisión de objeto \"" + str(strObj).decode(_stdin_encoding) + u"\": Exito]")
		else:
			# 4. Si el oyente no tiene ese nombre para el objeto en su inventario, la interaccion es un fracaso
			print (u"\t- [Termina revisión de objeto \"" + str(strObj).decode(_stdin_encoding) + u"\": Fallo]")
		# --------------------------------------
		# --------------------------------------
		# Resultados
		# Lista general de objetos
		listObjetosConNombre = {}
		for obj in listObjetos:
			listObjetosConNombre[obj] = []
		# Estado de los agentes
		print (u"2. Estado de los agentes")
		# Recorrer agentes
		for agent in listAgentes:
			# Imprimir estado del agente
			# agent.imprimirEstado()
			# Recorrer objetos
			for obj in listObjetos:
				# Recuperar lista de nombres del agente del objeto..
				listNomsAgent = agent.buscarNombresDe(obj)
				# Validar lista de nombres
				if listNomsAgent != None and 0 < len(listNomsAgent):
					# Recorrer nombres
					for nomAgent in listNomsAgent:
						# Ver existencia de nombre en lista
						if nomAgent not in listObjetosConNombre[obj]:
							# Agregar nombre a lista general
							listObjetosConNombre[obj].append(nomAgent)
		# Lista general de nombres
		listGenNoms = []
		# Recorrer objetos
		for obj in listObjetos:
			# Recuperar listaNoms
			listNames = listObjetosConNombre[obj]
			# Recorrer nombres
			for nomIL in listNames:
				# Validar
				if nomIL not in listGenNoms:
					# Agregar nombre a lista general de nombres
					listGenNoms.append(nomIL)
		# * El número total de nombres conocidos.
		print (u"3. Número total de nombres conocidos: \"" + str(len(listGenNoms)).decode(_stdin_encoding) + u"\"")
		# Recorrer lista general de objetos
		print (u"4. El número total de nombres para cada objeto es de...")
		for key, value in listObjetosConNombre.items():
			# * El número total de nombres para cada objeto.
			print (u"\t- Para el objeto \"" + key.decode(_stdin_encoding) + u"\" existen \"" + str(len(value)).decode(_stdin_encoding) + u"\" nombres")
		# Recorrer lista general de nombres
		numPdLdN = 0
		for nomDLG in listGenNoms:
			numPdLdN = numPdLdN + len(nomDLG)
		# * La longitud promedio de todos los nombres.
		print (u"5. La longitud promedio de todos los nombres es de: \"" + str(numPdLdN/len(listGenNoms)).decode(_stdin_encoding) + u"\"")
		# Imprimir lista general de arreglos
		print ("```json")
		print json.dumps(listObjetosConNombre, indent=4)
		print ("```")
		# Términa iteración
		print ("======")
else:
	print (u"Error: Se requieren 3 agumentos númericos: #n agente, #m objetos, #max_i maximo de interaciones.")
