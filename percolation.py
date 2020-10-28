# -*- coding: utf-8 -*-

import numpy as np
import random as rand
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from pylab import arange

def create_percolation_array(p):


	L=300
	S=np.zeros([L,L])
	for i in range(L):
		for j in range(L):
			S[i,j]= rand.random()
			if S[i,j]>=p:
				S[i,j]=0
			else:
				S[i,j]=1

	a= np.array(ndi.measurements.label(S), dtype='object')

	b=ndi.measurements.sum(S,a[0], index=arange(a[0].max()+1))

	return(a[0],b)

def check_if_perc(b):
	sum=0
	for i in range(np.shape(b)[1]):
		for j in range(np.shape(b)[1]):
			if(b[0,i]==b[np.shape(b)[1]-1,j] and b[0,i]!=0):
				return(1)

	return(0)

n=1000
probabilities=np.linspace(0.5, 0.65, 20)

percstats=[]
for p in probabilities:
	perc=[]
	print(p)
	for i in range(0,n):
		lw,b=create_percolation_array(p)
		perc.append(check_if_perc(lw)+check_if_perc(lw.T))
	percstats.append(perc)
	
np.savetxt("Perc_stats.txt", percstats)
