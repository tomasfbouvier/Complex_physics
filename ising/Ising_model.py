# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:26:47 2020

@author: Usuario
"""

import numpy as np
import random as rand
import matplotlib.pyplot as plt

#Defino configuracion inicial

k=20
nmax=300000
n0=0.8*nmax
n=0
T=200 # Kelvin
kb=1
M=0
Mexp=0
Mvec=[0]
H=0; J=T; h=0

S=np.zeros([k,k])
for i in range (np.shape(S)[0]):
    for j in range(np.shape(S)[1]):
        S[i,j] = rand.randint(-10000,10000)
        if(S[i,j]<0):
            S[i,j]=-1
        else:
            S[i,j]=1



for i in range (0,k-1):
    for j in range(0,k-1):
        H+= -J*S[i,j]*(S[i+1,j] + S[i,j+1])- h*S[i,j]
        M+= S[i,j]   
    H+= -J*S[k-1,i]*(S[k-1,i+1] + S[0,i])- h*S[k-1,i]
    H+= -J*S[i,k-1]*(S[i+1,k-1] + S[i,0])- h*S[i,k-1]
    M+= S[i,k-1] + S[k-1,i]
M-=S[k-1,k-1]   
H-= -J*S[k-1,k-1]*(S[0,k-1] + S[k-1,0])- h*S[k-1,k-1]

# Falta añadir frontera
R=0
cont=0
while(n<nmax):
    n+=1
    i= rand.randint(1,k-1); j= rand.randint(1,k-1)
    Saux=-S[i,j]
    if(i != k-1 and j != k-1):
        H2= H -( -J*S[i,j]*(S[i+1,j] + S[i,j+1]+S[i-1,j] + S[i,j-1])- h*S[i,j])
        H2+= ( -J*Saux*(S[i+1,j] + S[i,j+1] + S[i-1,j] + S[i,j-1])- h*Saux)

    else:
        if(i==k-1 and j!=k-1):
            H2= H -( -J*S[i,j]*(S[0,j] + S[i,j+1]+S[i-1,j] + S[i,j-1])- h*S[i,j])
            H2+= ( -J*Saux*(S[0,j] + S[i,j+1] + S[i-1,j] + S[i,j-1])- h*Saux)
        elif(j==1 and i!=k-1):
            H2= H -( -J*S[i,j]*(S[i+1,j] + S[i,0]+S[i-1,j] + S[i,j-1])- h*S[i,j])
            H2+= ( -J*Saux*(S[i+1,j] + S[i,0] + S[i-1,j] + S[i,j-1])- h*Saux)
        else:
            H2= H -( -J*S[i,j]*(S[0,j] + S[i,0]+S[i-1,j] + S[i,j-1])- h*S[i,j])
            H2+= ( -J*Saux*(S[0,j] + S[i,0] + S[i-1,j] + S[i,j-1])- h*Saux)
            
            
            
    deltaE= H2-H    
    if deltaE<0:
        S[i,j]=Saux
        H=H2
        M-= 2*S[i,j]
    else:   
        r= np.exp(-deltaE/(kb*T))
        q= rand.randint(0,100000000)/100000000
        if q<r:
            S[i,j]=Saux
            H=H2
            M-= 2*S[i,j]
      
   
    if n>n0:
        Mexp+=M

    Mvec.append(M/(k+1)**2)         
Mexp/= (nmax-n0)        
    
nvec=np.linspace(0,n,n+1)
plt.figure()    
plt.plot(nvec,Mvec)


plt.figure()
plt.imshow(S)

plt.show()


