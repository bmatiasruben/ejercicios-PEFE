#ComparaciÃ³n de Binomial y Poisson (df.uba.ar)
#Como entrada para ejecutar el programa dar valores para N y p de la Binomial
import numpy as np
from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math
import sys

n = float(sys.argv[1])  
p = float(sys.argv[2])
if len(sys.argv) > 3 :
    maxim = float(sys.argv[3])
else :
    maxim = n

# No uso mucho scripts, los defino por acá adentro
n = 20 
p = 0.6 

fig, ax = plt.subplots(1, 1, figsize=(14,6.20))

minim = 0
rango = maxim-minim
ax.set_xlim(left=minim-rango/100, right=maxim+rango/100)
ax.xaxis.set_ticks(range(minim, int(maxim)+1, 5))

text="$\mu$ = %3.2f" % (n*p)
plt.xlabel(text)

x = np.arange(0,n+1)
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
ax.vlines(x, 0, poisson.pmf(x, n*p), colors='r', lw=5, alpha=0.5)

plt.show()