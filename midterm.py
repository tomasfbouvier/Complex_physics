# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import numpy.random as rand


Ns=[]

Ns.extend(np.arange(10, 100, 1))
Ns.extend(np.arange(101, 1000, 1))
Ns.extend(np.arange(1001, 10000, 100))
Ns.extend(np.arange(10001, 100000, 500))

def finite_scaling_percolation(N,p, option):
#	N=int(N)
	C=np.zeros(N)

	for i in range(len(C)):
		if(np.random.rand()<p):
			C[i]=1

#	print(C)
	S=0.
	clusters=[]
	if(option=='1'):
		i=0
		while(i<len(C)-1):
			if(C[i]==C[(i+1)%N] and C[i]==1):
				S+=1.

			else:
	#			print(S/N)
				clusters.append(S)
				S=0.
			i+=1
	if(option=='2'):
		i=0
		while(i<len(C)-1):
			if(C[i]==C[(i+1)%N] and C[i]==1):
				S+=1.
			elif(C[i]==C[(i+2)%N] and C[i]==1):
				S+=1.
				i+=1
			else:
	#			print(S/N)
				clusters.append(S)
				S=0.
			i+=1
	if(len(clusters)==0):
		clusters.append(N)
	return(max(clusters))



p=np.linspace(0.001,0.99, 100)


s=[]

plt.figure()
for i in p:
#	print(i)
	print(finite_scaling_percolation(1000, i, '1'))
	plt.plot(i,finite_scaling_percolation(1000, i, '1')/1000., 'r.')
	plt.plot(i,finite_scaling_percolation(1000, i, '2')/1000., 'b.')

plt.plot(finite_scaling_percolation(1000, i, '1')/1000., 'r.', label="1 connection")
plt.plot(finite_scaling_percolation(1000, i, '2')/1000., 'b.', label="2 connections")

plt.legend(loc="best")
plt.show()




"""
Sx=[]


plt.figure()

for i in Ns:
#	print(i)
	plt.plot(float(finite_scaling_percolation(i, 0.3, '1'))/float(i), 1/float(i),'r.')
	plt.plot(float(finite_scaling_percolation(i, 0.3, '2'))/float(i), 1/float(i),'b.')
	
#	Sx.append(float(finite_scaling_percolation(i, 0.7, '1'))/float(i))

plt.plot(float(finite_scaling_percolation(i, 0.3, '1'))/float(i), 1/float(i),'r.' , label="1 conection")
plt.plot(float(finite_scaling_percolation(i, 0.3, '2'))/float(i), 1/float(i),'b.', label="2 connections ")

plt.xlabel("s")
plt.ylabel("1/N")
plt.legend(loc="best")
plt.show()

"""

def exercise_3(k,p, d='r'):
	G=nx.Graph()
	nodes= np.arange(0, k ,1)
	for i in range(len(nodes)):
		if(np.random.rand()<p):
			r=1
		else:
			r=0
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
					print("wey")
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


	for i in nodes:
		if( G.nodes[i]['ocupacy']==0):
			connections= [k for k in G.neighbors(i)]
			for j in connections:
				G.remove_edge(i,j)

	return(len(max(nx.connected_components(G), key=len)))

"""
p=np.linspace(0.01,0.99, 10)

N=[1000, 10000, 100000]
colours=['b.', 'y.', 'r.']

plt.figure()
for i in range(len(N)):
	c=colours[i]
	S=[]
	print(N[i])
	y=[]
	for j in p:
		print(exercise_3(N[i],j))
		aux=exercise_3(N[i],j)
		S.append(aux/N[i])
		y.append(j)
	plt.plot(y, S, c, markersize=3, label= N[i])

plt.xlabel("p")
plt.ylabel("S/N")
plt.legend(loc= 'best')
plt.show()

"""

"""
p=0.0
ps=[]
S=[]
while(p<1):
	p+=0.005
	ps.append(p)
	aux=None
	print(p)
	while(aux==None):
		aux=exercise_3(40, p)
	S.append(aux/40)

plt.figure()
plt.plot(ps, S, 'b.')
plt.show()


p=0.3

s=[]
y=[]
for i in Ns:
	print(i)
	aux= exercise_3(30,p)
	if(aux!=None):
		s.append(aux/i)
		y.append(1/i)

plt.figure()
plt.plot(s, y, 'b.')
plt.show()


"""
