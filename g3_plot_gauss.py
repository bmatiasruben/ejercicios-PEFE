import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

mu = 0
variance = 1
sigma = math.sqrt(variance)

x = np.linspace(mu - 5*sigma, mu + 5*sigma, 100)

plt.plot(x, scipy.stats.norm.pdf(x, 0, 1))
# Agrego las otras Gaussianas para tener todo al mismo tiempo
plt.plot(x, scipy.stats.norm.pdf(x, 0, 2), 'g-')
plt.plot(x, scipy.stats.norm.pdf(x, 1, 1), 'r.')

plt.show()