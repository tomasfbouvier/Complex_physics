# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt




M=np.zeros(100)

for i in range(len(M)):
	M[i]=np.random.rand()


t=0
tvec=[]
minvec=[]
maxminvec=[]
aux=0
while t<10**6:
	t+=1
	tvec.append(t)
	B=M[M.argmin()]
	minvec.append(B)
	M[M.argmin()]= np.random.rand()
	i= np.random.randint(len(M))
	M[i]=np.random.rand()
	
	if B>aux:
		aux=B
	
	maxminvec.append(aux)


plt.figure()
#plt.hist(M, bins=20)
plt.plot(tvec, minvec, 'b.')
plt.show()


plt.figure()
plt.plot(tvec, maxminvec, 'b.')
plt.show()
