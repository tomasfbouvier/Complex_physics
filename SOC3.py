# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt



k=100
M=np.zeros(k)

for i in range(len(M)):
	M[i]=np.random.rand()


t=0
tvec=[]
minvec=[]
maxminvec=[]
aux=0

mu=0.05

while t<10**(7):
	dt=10**(8)
	side=-1
	for i in range(len(M)):
		rand = np.random.rand()
		aux= -np.log(np.random.rand())*np.e**(M[i]/mu)
		
		if aux<dt:
			dt=aux
			arg=i 		
			if rand>0.5:
				side=1

	M[arg]= np.random.rand(); M[(arg+side)%k]=np.random.rand()
	tvec.append(t)
	minvec.append(arg)
	t+=dt


plt.figure()
#plt.hist(M, bins=20)
plt.plot(minvec, tvec, 'b.')
plt.show()


"""

plt.figure()
plt.plot(tvec, maxminvec, 'b.')
plt.show()


"""
