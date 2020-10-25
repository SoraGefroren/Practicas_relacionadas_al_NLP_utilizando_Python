# Librerias
import numpy as np
import pandas as pd

# Librerias

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

# Función para generar un Vector_FALSO
def generar_v_falso(v_test):
    # Obtener tamaño
    llave_masc = 0
    valor_masc = 0
    tam_vector = len(v_test)
    vFalso = []
    diccvc = {}
    # Contar concurrentecia de elementos
    for vv in v_test:
        # Validar 
        if vv not in diccvc:
            diccvc[vv] = 1
        else:
            diccvc[vv] += 1
    # Obtener el valor mas concurrente
    for key, value in diccvc.items():
        # Validar
        if valor_masc < value:
            llave_masc = key
            valor_masc = value
    # Generar vector falso
    for i in range(tam_vector):
        vFalso.append(llave_masc)
    # Regresar vector
    return vFalso

# Función para clasificar
def clasifi_raw(documento, panda_raw, dicc_palporator, ary_terms, vectorizer_x):
    # Preparar arreglo Nummpy
    X_vectors = np.array([])
    # Recorrer arreglo panda de textos
    for indice in range(len(panda_raw)):
        # Recuperar autor
        txt_autor = documento['autor'].iloc[indice]
        # Validar tamaño de vector
        if len(X_vectors) == 0:
            X_vectors = vectorizer_x(panda_raw, dicc_palporator, ary_terms, txt_autor, indice)
        else:
            X_vectors = np.vstack([X_vectors, vectorizer_x(panda_raw, dicc_palporator, ary_terms, txt_autor, indice)])
    # Generar arreglo basado en basado en los tipos que contiene
    y = documento['autor'].to_numpy()
    # Recortar X_Vector para generar los TRAIN y TEST
    X_train, X_test, y_train, y_test = train_test_split(X_vectors, y, test_size = 0.3, random_state = 101)
    
    # Analisis de regresión - Entrenamiento
    logregTrainLR = LogisticRegression()
    logregTrainLR.fit(X_train, y_train)

    # Analisis KNN - Entrenamiento
    logregTrainKNN = KNeighborsClassifier(n_neighbors=10)
    logregTrainKNN.fit(X_train, y_train)

    # Analisis SVN - Entrenamiento
    logregTrainSVN = SVC(kernel='linear')
    logregTrainSVN.fit(X_train, y_train)

    #score = cross_val_score(logregTrainSVN, X_vectors, y, cv=5)
    #print(score)

    # Analisis de regresión - Linea base
    # logregBL = LogisticRegression()
    # logregBL.fit(X_test, y_test)
    
    # Calcular predicción
    y_predTrainLR = logregTrainLR.predict(X_test)
    y_predTrainKNN = logregTrainKNN.predict(X_test)
    y_predTrainSVN = logregTrainSVN.predict(X_test)

    # y_predBL = logregBL.predict(X_train)
    # Obtener y_falsa
    y_falsa = generar_v_falso(y_test)
    
    # Devolver resultado
    return y_test, y_falsa, y_predTrainLR, y_predTrainKNN, y_predTrainSVN

# Función para clasificar y construir vector de caracteristicas
def clasifi_vector(documento, panda_raw, dicc_palporator, ary_terms, vectorizer_xy):
    # Preparar arreglo Nummpy
    X_vectors = np.array([])
    Y_vectors = np.array([])
    Z_vectors = np.array([])
    W_vectors = np.array([])
    XTempV = np.array([])
    YTempV = np.array([])
    ZTempV = np.array([])
    WTempV = np.array([])
    # ID autores
    diccIDAtors = {}
    diccIDTrms = {}
    contIDAtor = 1
    contIDTerm = 1
    AutorsAry = []
    # Recorrer arreglo panda de textos
    for indice in range(len(panda_raw)):
        # Recuperar autor
        txt_autor = documento['autor'].iloc[indice]
        # Validar y resguardar ID de autor
        if txt_autor not in diccIDAtors:
            diccIDAtors[txt_autor] = contIDAtor
            contIDAtor += 1
        # Agregar ID de autor en arreglo
        AutorsAry.append(diccIDAtors[txt_autor])
        # Validar tamaño de vector
        if len(X_vectors) == 0:
            X_vectors, Y_vectors, Z_vectors, W_vectors, diccIDTrms, contIDTerm = vectorizer_xy(panda_raw, dicc_palporator, ary_terms, txt_autor, indice, diccIDAtors, diccIDTrms, contIDTerm)
        else:
            XTempV, YTempV, ZTempV, WTempV, diccIDTrms, contIDTerm = vectorizer_xy(panda_raw, dicc_palporator, ary_terms, txt_autor, indice, diccIDAtors, diccIDTrms, contIDTerm)
            X_vectors = np.vstack([X_vectors, XTempV])
            Y_vectors = np.vstack([Y_vectors, YTempV])
            Z_vectors = np.vstack([Z_vectors, ZTempV])
            W_vectors = np.vstack([W_vectors, WTempV])
    # Ajuste
    P_vectors = np.array(ary_terms)
    ID_rw_P = []
    contaIPD = 1
    for tempW in P_vectors:
        ID_rw_P.append(contaIPD)
        contaIPD += 1
    # Regresar RW
    return X_vectors, Y_vectors, Z_vectors, W_vectors, P_vectors, ID_rw_P, AutorsAry

# Función para generar vector de caracteristicas
def gen_vector_raw (list_stopwords, documento, panda_raw, vectorizer_xy, gen_z_elements):
    # Generar diccionario global
    Z_palcon_ator_term, Z_palcon_term_ator, Z_aryterms = gen_z_elements(list_stopwords, documento)
    # Clasificar elementos en arreglo Panda
    n1_raw, n2_raw, n3_raw, n4_raw, n5_raw, n6_raw, n7_raw = clasifi_vector(documento, panda_raw, Z_palcon_ator_term, Z_aryterms, vectorizer_xy)
    # Devolver resultado
    return n1_raw, n2_raw, n3_raw, n4_raw, n5_raw, n6_raw, n7_raw

# Función para generar y_pred y y_test
def predictor_test (list_stopwords, documento, panda_raw, vectorizer_x, gen_z_elements):
    # Generar diccionario global
    Z_palcon_ator_term, Z_palcon_term_ator, Z_aryterms = gen_z_elements(list_stopwords, documento)
    # Clasificar elementos en arreglo Panda
    y_test, y_falsa, y_predLR, y_predKNN, y_predSVN = clasifi_raw(documento, panda_raw, Z_palcon_ator_term, Z_aryterms, vectorizer_x)
    # Devolver resultado
    return y_test, y_falsa, y_predLR, y_predKNN, y_predSVN