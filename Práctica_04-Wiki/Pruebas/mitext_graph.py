# -*- coding:utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import random

# Crea grafica
G = nx.DiGraph()

# Lista de nodos
misNodos = ["Hola", "Mundo", "Mundial", "Adios"]

# Vertices
G.add_nodes_from(misNodos)

# Aristas
aristas = [("Hola","Mundo"), ("Hola","Mundial"), ("Hola","Adios"), ("Adios", "Mundo"), ("Adios", "Mundial")]
G.add_edges_from(aristas)

pos=nx.spring_layout(G)
nx.draw_networkx_labels(G, pos, labels=dict([(i,i) for i in misNodos]))

# Dibuja la gráfica
nx.draw(G,pos)

# Muestra en pantalla lo dibujado
plt.show()
