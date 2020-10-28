# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def count_elements(M, element):
	number_of_elements=0
	for i in range(len(M)):
		if (M[i]== element):
			number_of_elements+=1
	return(number_of_elements)


M= np.zeros(10000)

#0 suspicious
#1 infected
#> 15 recovered

t=0

dt=10 #days

k=0
while(k<100):
	k=count_elements(M, 1)
	i= np.random.randint(len(M))
	if(M[i]==0):
		M[i]=1

contagios=[]
ts=[]
while(t<1000):
	for i in range(len(M)):
		if(M[i]>0 and M[i]<10):
			aux=1
			while(aux!=0):
				j=np.random.randint(len(M))
				aux=M[j]
			if(np.random.rand()<0.1):
				M[j]=1
			M[i]+=1

	t+=dt/2
	ts.append(t)
#evaluate change
	aux=0
	for i in range(len(M)):
		if(M[i]>0 and M[i]<10):
			aux+=1

	contagios.append(aux)


plt.figure()
plt.plot(ts, contagios)
plt.show()
