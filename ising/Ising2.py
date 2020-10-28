#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Created on Sat Aug 29 18:26:47 2020

@author: Usuario
"""

import numpy as np
import random as rand
import matplotlib.pyplot as plt
import numba as nb

#Defino configuracion inicial

k=20
Ts=np.array(np.linspace(0.5, 3, 15)) # Kelvin
Ts=np.hstack([Ts,np.array(np.linspace(3.1,4,50))])
Ts=np.hstack([Ts,np.array(np.linspace(4, 10,15))])

Ts=np.array(np.linspace(0.5, 15, 20))


nmax=500000
n0=0.8*nmax

kb=1.
J=1.; h=1;
Mvec=[]
Hvec=[]

@nb.njit
def Monte_ising(T, h, n0, nmax):
	M=0.
	Mexp=0.; Eexp=0.
	H=0.; M=0.

	S=np.zeros([k,k])
	for i in range (np.shape(S)[0]):
	    for j in range(np.shape(S)[1]):
	        S[i,j] = rand.randint(-10000,10000)
	        if(S[i,j]<0):
	            S[i,j]=-1
	        else:
	            S[i,j]=1


	size=np.shape(S)
	for i in range(size[0]):
		for j in range(size[1]):
			M+=S[i,j]
			H+=-1./2.*J*(S[i,(j-1)%k]+S[(i+1)%k,j]+S[(i-1)%k,j]+S[i,(j+1)%k])+h*S[i,j]
	n=0
	vecH=[]
	vecM=[]

	while (n<nmax):
		n+=1
		i=rand.randrange(0,k,1);j=rand.randrange(0,k,1)	
		dE = +2*J*S[i,j]*(S[(i-1)%k,j]+S[(i+1)%k,j]+S[i,(j-1)%k]+S[i,(j+1)%k])-2*h*S[i,j]
		if(dE<=0):
			S[i,j]*=-1
			M+= 2*S[i,j]
			H+=dE
		else:
			r=np.e**(-dE/(kb*T))
			q=rand.random()
			if r>q:
				S[i,j]*=-1
				M+= 2*S[i,j]
				H+=dE

		if(n>n0):
			Mexp+=M/k**2
			Eexp+= H
	return (abs(Mexp/(n-n0)), abs(Eexp/(n-n0)))

"""
# 3.

nmax= 1000000
T=2

n0= np.linspace(0.2, 0.99, 40)
for i in n0:
	aux=Monte_ising(T,h, i*nmax, nmax)
	Mvec.append(aux[0])
	Hvec.append(aux[1])

np.savetxt("M_n0.txt",Mvec)
np.savetxt("H_n0.txt",Hvec)

plt.figure()
plt.plot(n0, Mvec, 'b.')
plt.xlabel("n0")
plt.ylabel("<M>")
plt.show()
plt.figure()
plt.plot(n0,Hvec,'b.')
plt.xlabel("n0")
plt.ylabel("E")
plt.show()
"""

# 4.
for T in Ts:
	Mvec.append(Monte_ising(T,h, n0, nmax)[0])
	Hvec.append(Monte_ising(T,h, n0,nmax)[1])
np.savetxt("M.txt",Mvec)
np.savetxt("H.txt",Hvec)

plt.figure()
plt.plot(Ts, Mvec, 'b.')
plt.xlabel("KbT/J")
plt.ylabel("<M>")
plt.show()
plt.figure()
plt.plot(Ts,Hvec,'b.')
plt.xlabel("KbT/J")
plt.ylabel("<H>")
plt.show()

"""
# 5.

Ts=np.array(np.linspace(0.5, 2, 10)) # Kelvin
Ts=np.hstack([Ts,np.array(np.linspace(2.1,3,10))])
Ts=np.hstack([Ts,np.array(np.linspace(3.1,5,10))])

samples=10
Marray=[]
Harray=[]
i=0
while i< samples:	
	i+=1
	Mvec=[];Hvec=[]
	for T in Ts:
		aux=Monte_ising(T,h, n0, nmax)
		Mvec.append(aux[0])
		Hvec.append(aux[1])
	Marray.append(Mvec)
	Harray.append(Hvec)

Marray =np.array(Marray)
Harray =np.array(Harray)
np.savetxt("M_stats", Marray)
np.savetxt("H_stats", Harray)
Mmeans=[]
Mstd=[]
Hmeans=[]
Hstd=[]
for i in range(np.shape(Marray)[1]):
	Mmeans.append(np.mean(Marray[:,i]))
	Mstd.append(np.std(Marray[:,i]))
	Hmeans.append(np.mean(Harray[:,i]))
	Hstd.append(np.std(Harray[:,i]))
	


plt.figure()
plt.plot(Ts,Mmeans, 'b.')
plt.errorbar(Ts,Mmeans, yerr= Mstd , fmt = 'b.', capsize=3, alpha=.6 )
plt.show()

plt.figure()
plt.plot(Ts,Hmeans, 'b.')
plt.errorbar(Ts,Hmeans, yerr= Hstd , fmt = 'b.', capsize=3, alpha=.6 )
plt.show()

"""
"""
#6 

Marray=np.loadtxt("M_stats", unpack=True)
Mmeans=[]
Mstd=[]
Hmeans=[]
Hstd=[]
for i in range(np.shape(Marray)[1]):
        Mmeans.append(np.mean(Marray[:,i]))
        Mstd.append(np.std(Marray[:,i]))

plt.figure()
plt.plot(Ts,Mmeans, 'b.')
plt.errorbar(Ts,Mmeans, yerr= Mstd , fmt = 'b.', capsize=3, alpha=.6 )
plt.show()

"""
