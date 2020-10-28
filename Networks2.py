# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G=nx.Graph()
for i in range(5000):
	G.add_node(i)
	N=G.number_of_nodes()
	p=2./(N+1.)
	for j in range(N-1):
	#	p=P*((G.degree[j]+1.)/N)
		r=np.random.rand()
		if(r<p):
			G.add_edge(i,j)
			break
"""
	if(N>1000):
		ListOfNodes = list(G.nodes())
		s=ListOfNodes[np.random.randint(len(ListOfNodes))]
		G.remove_node(s)
"""


print(nx.number_connected_components(G))

a=[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]

nx.draw(G, node_size=5000/N)
#plt.figure()
#plt.hist(a,300, density=True)
print(a)

plt.show()

