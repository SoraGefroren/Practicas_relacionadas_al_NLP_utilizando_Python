#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3.1. Ejercicio: Suma de enteros
isNum = True
while isNum:
    try:
        myNum = input((u"Ingresa un número: ").encode('utf-8'))
        if type(myNum) == str:
            isNum = False
            break
        if type(myNum) == int:
            otNum = myNum - 1
            while 0 < otNum:
                myNum = myNum + otNum
                otNum = otNum - 1
        else:
            isNum = False
        print ("Resultado: " + str(myNum))
    except:
        isNum = False
        print("Ocurrio un error.")