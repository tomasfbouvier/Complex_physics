# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def sigmoid(x,a,b):
	return(1/(1+np.e**(-a*(x-b))))

plt.figure()
def analize(string, colour):
		
	perc=np.loadtxt(string, unpack=True)

	perc_mean=[]
	perc_error=[]
	for i in range(np.shape(perc)[1]):
		perc_mean.append(np.mean(perc[:,i])/2)
		perc_error.append(np.std(perc[:,i])/2)

	probabilities=np.linspace(0.5, 0.65, 20)

	plt.plot(probabilities, perc_mean, colour, label="data")
	plt.errorbar(probabilities, perc_mean, yerr= perc_error , fmt = colour, capsize=3, alpha=.6 )

	x=np.linspace(0.5, 0.65, 1000)
	
	return(probabilities, perc_mean, perc_error)

def fit(probabilities,means, errors, colour):

	probabilities2=[]; means2=[]; errors2=[]

	for i in range(len(probabilities)):
		if(errors[i]!=0):
			probabilities2.append(probabilities[i])
			means2.append(means[i])
			errors2.append(errors[i])

	p,pcov=opt.curve_fit(sigmoid, probabilities2, means2, sigma=errors2, p0=[1,0.6])

	x=np.linspace(0.5, 0.65, 1000)

	plt.plot(x, sigmoid(x,p[0],p[1]), colour, label="sigmoid fit")
	return(p, np.sqrt(np.diagonal(pcov)[:]))


p100,m100, e100 =analize("Perc_stats_100_10000.txt", 'b.')
p200,m200,e200 =analize("Perc_stats_200_1000.txt", 'r.')
p150, m150, e150 = analize("Perc_stats_150_1000.txt", 'y.')
p50, m50, e50 = analize("Perc_stats_50_1000.txt", 'g.')
p300,m300,e300= analize("Perc_stats_300_1000.txt", 'm.')

print("50",fit(p50,m50,e50, 'g-'))
print("100",fit(p100,m100,e100, 'b-'))
print("150",fit(p150,m150, p150, 'y-'))
print("200",fit(p200, m200, e200, 'r-'))
print("300", fit(p300,m300, e300, 'm-'))

plt.xlabel("p")
plt.ylabel("percolation rate")
plt.legend(loc="best", fontsize=9)
plt.savefig("perc_def.png")
plt.show()
