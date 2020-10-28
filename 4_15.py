# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def racional(x):
	return 1/x**(1.5)

def main(S):
	iter=0
	while(iter<3000000):
		iter+=1
		i= np.random.randint(0,size)
		j= np.random.randint(0,size)
		S[i]+=S[j]; S[j]=1
	return(S)

size=1000
S=1*np.random.rand(size)

main(S)

S=list(S)
while(max(S)>100):
	S.remove(max(S));

x=np.linspace(1,100, 10000)

plt.figure()
plt.hist(S, bins=100)
plt.plot(x, 500*racional(x))
plt.show()
