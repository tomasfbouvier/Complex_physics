# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import networkx.drawing.nx_pylab as drawer

N=100
links=150

G=nx.dense_gnm_random_graph(100, 150)

nx.draw(G, node_size=50)
plt.show()


print("haasdwek", list(max(nx.connected_component_subgraphs(G), key=len)))

Gcs=[]
iss=[]

i=0



while(i<N):

	i+=1

	n=np.random.randint(0, len(list(G.nodes)))

	G.remove_node(list(G.nodes)[n])

	Gc = max(nx.connected_component_subgraphs(G), key=len)

	iss.append(N-i)
	Gcs.append(Gc)

plt.plot(iss,Gcs)
plt.show()


