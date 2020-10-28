# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def racional(x):
	return 1/x**(1.5)

def main(S):
	iter=0
	while(iter<3000000):
		aux=-1
		contador=0
		while(aux<0):
			contador+=1	
			i= np.random.randint(0,size)
			j= np.random.randint(0,size)
			aux=S[i]
			if(aux>=0):
				aux+=S[j]-1
			if(contador==10**5):
				return(S)
		S[i]=aux
		S[j]= np.random.randint(0,3)
		iter+=1
		if(iter%1000==0):
			print(iter)
	return(S)

size=1000
S=1*np.random.rand(size)

main(S)

S=list(S)
print(max(S))

"""
while(max(S)>100):
	S.remove(max(S));
"""
x=np.linspace(0.11,max(S), 10000)

plt.figure()
plt.hist(S, bins=100)
plt.plot(x, 500*racional(x))
plt.show()
