# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import scipy.optimize as opt

M= np.zeros([50,50])

for i in range(np.shape(M)[0]):
	for j in range(np.shape(M)[0]):
		M[i,j]= rand.randint(0,6)

def line(x,a,b):
	return(a*x+b)


def rational(x,a,b):
	return(a/x**b)

def check_change(i,j):
	if(M[i,j]>=4):
		M[i,j]-=4;
		if(i<np.shape(M)[0]-1):
			M[i+1,j]+=1
		if(j<np.shape(M)[1]-1):
			M[i, j+1]+=1
		if(i>0):
			M[i-1,j]+=1
		if(j>0):
			M[i, j-1]+=1
		k=1
	else:
		k=0
	return(k)

def check_equilibrium(M): 
	k=False
	for i in range(np.shape(M)[0]):
		for j in range(np.shape(M)[1]):
			if(M[i,j]>=4):
				k=True
	return(k)


t=0; dt=0.1; tmax=1

size=[]
	
while(t<=tmax):
	t+=dt
	sizeaux=0
	while (check_equilibrium(M)==True):
		for i in range(np.shape(M)[0]):
			for j in range(np.shape(M)[1]):
				sizeaux+= check_change(i,j)
	
	i=rand.randint(0,np.shape(M)[0]); j=rand.randint(0, np.shape(M)[1])
	M[i,j]+=1
	size.append(sizeaux)
	if(t%10==0):
		print(t)

size.remove(size[0])

with open("SOC.txt", "ab") as f:
    np.savetxt(f, size)

size=np.loadtxt("SOC.txt", unpack=True)


plt.figure()
plt.hist(size, 100)
plt.show()



"""
size=size[size!=0]


bins= np.linspace(min(size), max(size), 100)

#bins= np.logspace(0, 4, 20)
#xline=np.logspace(0,4, 100)
xline=np.linspace(bins, max(size), 1000)
frequencies, bins =np.histogram(size, bins)

binslog=np.log(bins[bins<np.e**(8)])

freqlog=np.log(frequencies[:len(binslog)])


p,pcov=opt.curve_fit(line, binslog[1:], freqlog[1:])
xline=np.linspace(min(binslog), max(binslog),100)

print("p", p)

plt.figure()
plt.plot(binslog[:], freqlog[:],'b.')
plt.plot(xline, line(xline, p[0],p[1]))
plt.show()

print(bins)
print(frequencies)

p,pcov=opt.curve_fit(rational, bins[:-1], frequencies[:])

print(p)
plt.figure()
plt.hist(size, bins=bins, density=False)
plt.plot(xline, rational(xline, p[0], p[1]))
plt.show()
"""
