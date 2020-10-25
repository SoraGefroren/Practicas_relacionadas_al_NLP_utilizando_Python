#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import random

_stdin_encoding = sys.stdin.encoding or 'utf-8'

# 3.3. Ejercicio: Ahorcado
class Ahorcado:
    # Constructor
    def __init__(self, p, E):
        # Palabra objetivo
        self.p = p
        self.pTemp = ""
        # Ajuste
        numC_ofP = len(self.p)
        for i in range(numC_ofP):
            self.pTemp = self.pTemp + "_"
        # Máximo de intentos
        self.E = E
        self.eCont = 0
    
    # Jugar
    def jugar (self, c):
        # Contar coincidencias
        if (0 < self.p.count(c)):
            numC_ofP = len(self.p)
            for i in range(numC_ofP):
                if (self.p[i] == c):
                    self.pTemp = self.pTemp[:i] + c + self.pTemp[(i+1):]
        else:
            self.eCont = self.eCont + 1 # Sumar intento
    # Estado
    def estado (self):
        numC_ofP = len(self.pTemp)
        for i in range(numC_ofP):
            print self.pTemp[i] + " ",
        if (self.puedeContinuar()):
            if (self.lograsteGanar()):
                print ("(ganaste)\n")
            else:
                print ("(" + str(self.E - self.numErrores()) + " errores posibles)\n")
        else:
            if (self.lograsteGanar()):
                print ("(ganaste)\n")
            else:
                print ("(perdiste)\n")
    
    # Número de errores
    def numErrores (self):
        return self.eCont # Devolver número de intentos

    # Validación 1
    def puedeContinuar (self):
        if (self.eCont < self.E):
            return True
        else:
            return False
    
    # Validación 2
    def lograsteGanar (self):
        if (self.p == self.pTemp):
            return True
        else:
            return False

    # Ejecución
    def ejecutar (self):
        # Ciclo
        while self.puedeContinuar() and not self.lograsteGanar():
            # Obtener letra
            letra = raw_input("Introduzca una letra: ").decode(_stdin_encoding)
            # Validar
            if 1 < len(letra):
                letra = list(letra)[0]
            # Jugar
            self.jugar(letra)
            self.estado()

# Instanciar clase
myList = ["fresa", "uva", "pera", "sandia", "manzana", "durazano", "mora", "melon"]
ahorcado = Ahorcado(random.choice(myList), random.randint(3, 7))
ahorcado.ejecutar()