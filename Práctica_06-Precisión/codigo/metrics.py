# Librerias
import numpy as np
import pandas as pd

# Formula de presición
def precision(predicted, baseline):
	# Obtener maximos
	maxPD = len (predicted)
	maxBL = len (baseline)
	maxR = 0
	# Seleccionar maximo
	if maxPD < maxBL:
		maxR = maxPD
	else:
		maxR = maxBL
	# 
	r_presicion = 0
	# Recorrer areglo
	for i_ary in range(maxR):
		if i_ary < maxPD and i_ary < maxBL:
			if predicted[i_ary] == baseline[i_ary]:
				r_presicion += 1
	# Validar resultado
	if r_presicion > 0:
		r_presicion = r_presicion/maxR
	# Regresar resultado
	return r_presicion