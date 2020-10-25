#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

_stdin_encoding = sys.stdin.encoding or 'utf-8'

# 3.2. Ejercicio: Lenguaje de la F
isStr = True
while isStr:
    myCad = raw_input("Ingresa una cadena: ").decode(_stdin_encoding)
    try:
        if myCad == "S":
            isStr = False
            break
        
        myCad = myCad.replace("a", "afa")
        myCad = myCad.replace("e", "efe")
        myCad = myCad.replace("i", "ifi")
        myCad = myCad.replace("o", "ofo")
        myCad = myCad.replace("u", "ufu")

        myCad = myCad.replace(u"á", u"áfa")
        myCad = myCad.replace(u"é", u"éfe")
        myCad = myCad.replace(u"í", u"ífi")
        myCad = myCad.replace(u"ó", u"ófo")
        myCad = myCad.replace(u"ú", u"úfu")            

        myCad = myCad.replace("by", "byfi")
        myCad = myCad.replace("cy", "cyfi")
        myCad = myCad.replace("dy", "dyfi")
        myCad = myCad.replace("gy", "gyfi")
        myCad = myCad.replace("hy", "hyfi")
        myCad = myCad.replace("jy", "jyfi")
        myCad = myCad.replace("ky", "kyfi")
        myCad = myCad.replace("ly", "lyfi")
        myCad = myCad.replace("my", "myfi")
        myCad = myCad.replace("ny", "nyfi")
        myCad = myCad.replace("py", "pyfi")
        myCad = myCad.replace("qy", "qyfi")
        myCad = myCad.replace("ry", "ryfi")
        myCad = myCad.replace("sy", "syfi")
        myCad = myCad.replace("ty", "tyfi")
        myCad = myCad.replace("vy", "vyfi")
        myCad = myCad.replace("wy", "wyfi")
        myCad = myCad.replace("xy", "xyfi")
        myCad = myCad.replace("zy", "zyfi")

        print (u"Resultado: " + myCad)
    except:
        isStr = False
        print("Ocurrio un error.")