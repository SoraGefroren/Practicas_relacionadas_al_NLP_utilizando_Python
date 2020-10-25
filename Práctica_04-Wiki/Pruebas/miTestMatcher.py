
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

# Refinir expresiones regulares
patron_1 = re.compile('(las|la|los|el){1} (\w+) (son un|son una|es un|es una|fueron un|fuerona una|fue un|fue una){1} (\w+)')
patron_2 = re.compile('(\w+) (tal como|así como|como por|por ejemplo|tal como:|como:|como){1} (\w+)*(,\s*\w+)*(\s*y\s*\w+)*')
patron_2_1 = re.compile('(\w+) (tal como|así como|como por|por ejemplo|tal como:|como:|como){1} (\w+)(.*)(#|$)')
patron_2_2 = re.compile('(\w+)(,\s*\w+)*(\s*y\s*\w+)')
patron_3 = re.compile('(\w+) (es|forma|forman|son){1} (parte){1} (del|de las|de los|de el|de una|de un|de){1} (\w+)')
patron_4 = re.compile('(\w+)(\s*le|\s*es|\s*son)* (perteneciente(s)*|pertenecen|pertenece|a){1} (la|al|a)* (\w+)')
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
#print (patron_1.search("Así, como la historia es una reliquia en el tiempo, los ancestros son un libro abierto"))
#print (patron_1.findall("Así, como la historia es una reliquia en el tiempo, los ancestros son un libro abierto"))
#print (patron_1.match("Así, como la historia es una reliquia en el tiempo, los ancestros son un libro abierto"))
#print("-------------------------------------------------------------------------")
#print (patron_2.search("El dibujo tal como: pitura, escultura, trazado y grabado, son arte"))
print (patron_2.findall("El dibujo tal como: pitura y grabado, son arte"))
#print (patron_2.match("El dibujo tal como: pitura, escultura, trazado y grabado, son arte"))
print (patron_2_2.findall("El dibujo tal como: pitura, escultura, trazado y grabado, son arte"))
#print("-------------------------------------------------------------------------")
#print (patron_3.search("Las islas forman parte del ocenano y la tierra es parte de estrellas y dios forma parte de un todo"))
#print (patron_3.findall("Las islas forman parte del ocenano y la tierra es parte de estrellas y dios forma parte de un todo"))
#print (patron_3.match("Las islas forman parte del ocenano y la tierra es parte de estrellas y dios forma parte de un todo"))
#print("-------------------------------------------------------------------------")
#print (patron_4.search("Las guerras perteneciente al caos"))
#print (patron_4.findall("Las guerras a la caos"))
#print (patron_4.match("Las guerras perteneciente al caos"))
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")