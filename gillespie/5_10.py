# -*- coding: utf-8 -*-

#dx/dt= 12-x

import numpy as np
import matplotlib.pyplot as plt

t=0
x=0.1
r1=12.


plt.figure()
events=0
while events<1000:
	r2= x

	dt1= -4./r1*np.log(np.random.rand())
	dt2= -1./r2*np.log(np.random.rand())

	dt=min([dt1,dt2])

	if(dt==dt1):
		x+= 4.
	else:
		x-=1.
		
	t+=dt
	print(t)
	plt.plot(t,x, 'b.')
	events+=1
plt.show()

