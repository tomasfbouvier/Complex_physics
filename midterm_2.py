# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import numpy.random as rand



def Ising(G, T):

	J=1.
	nodes= list(G.nodes())
	t=0.
	tmax= 10000.
	size=len(nodes)
	M=[]
	while(t<tmax):
		i=np.random.randint(0, k)
		dE=0
		connections= [k for k in G.neighbors(nodes[i])]
		for j in connections:
			if(-nx.get_node_attributes(G,'ocupacy')[i]!=nx.get_node_attributes(G,'ocupacy')[j]):
				dE+=J
			else:
				dE-=J
		dE*=2.
		if(dE<=0):
			G.nodes[i]['ocupacy']*=-1
		else:
			r= np.e**(-dE/T)
			if(r>np.random.rand()):
				G.nodes[i]['ocupacy']*=-1
		if(t> 0.98*tmax):
			M.append(sum(list(nx.get_node_attributes(G,'ocupacy').values())))
		t+=1.
	return(M)

def lattice(k, p, d='1'):

	G=nx.Graph()
	nodes= np.arange(0, k ,1)
	for i in range(len(nodes)):
		if(np.random.rand()<p):
			r=1.
		else:
			r=-1.
		G.add_node(nodes[i], ocupacy= r);

	if(d=='r'):
		aux=False
		for i in nodes: 
			iter=0 
			while(G.degree(i)<2):
				j=rand.randint(0, k)
				iter+=1
				if(G.degree(j)<2 and abs(i-j)>1 and (j in G.neighbors(i))==False):
					G.add_edge(i,j)
				if(iter>= 1000):
					aux=True
					break
		if(aux==True):
			for i in nodes:
				if(G.degree(i)<2):
					for j in nodes:
						if(G.degree(j)<2 and abs(i-j)>1 and (j in G.neighbors(i))==False):
							G.add_edge(i,j)
	for i in range(len(nodes)):
		G.add_edge(nodes[i], nodes[(i+1)%k]);
		if(d=='2'):
			G.add_edge(nodes[i], nodes[(i+2)%k]);

	return(G)

k=400
p=0.5 #Just initial proability

Ts1=[0.1, 0.25, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.25,2., 3., 4., 4.5] 
Ts2=[0.1,0.5, 1, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.5, 3., 3.5, 4., 4.5]
Tsr= [0.1,0.5,1., 1.5, 2., 2.2, 2.4, 2.6, 2.8,3., 3.2, 3.4, 4, 4.5]

plt.figure()

def exercise2(Ts, mode, c):

	Ms=[]
	Merr=[]
	for T in Ts:
		print(T)
		G= lattice(k, p, mode)
		M= Ising(G,T)
		t= np.linspace(0, len(M), len(M))
#		plt.figure()
#		plt.plot(t,M, 'b.')
#		plt.show()
		Ms.append(abs(np.mean(M)/k))
		print(Ms)
		Merr.append(np.std(M)/k)


	print(Ms)
	plt.plot(Ts, Ms, c, label= mode)
	plt.errorbar(Ts,Ms, yerr= Merr , fmt = c, capsize=3, alpha=.6 )
	return None 

exercise2(Ts1, '1', 'y')
exercise2(Ts2,'2', 'r')
exercise2(Tsr, 'r', 'b')

plt.xlabel("T (K) ")
plt.legend( loc="best")
plt.ylabel("< $ s_{i} $ >")
plt.show()
