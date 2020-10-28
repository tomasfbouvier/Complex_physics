# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x=-np.log(np.random.rand(100000))

plt.hist(x, bins=100)

xs=np.linspace(min(x), max(x), 10000)

plt.plot(xs,11000*np.e**(-xs))
plt.show()
