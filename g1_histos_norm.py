#http://users.df.uba.ar/maurosilber/incertezas/histogramas.html
import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt
#matplotlib inline

np.random.seed(42) # Para obtener la misma secuencia de numeros aleatorios
X = poisson(mu=4.5) # Defino una variable aleatoria con distribucion de Poisson de parametro 4.5
Xi = X.rvs(size=1000) # Genero 1000 numeros de la variable aleatoria

Y, bins = np.histogram(Xi, bins=np.arange(0, Xi.max())) # Genero el histograma

f, ax = plt.subplots(ncols=3, figsize=(16,4), sharey=True) # Leer como Share Y
f.subplots_adjust(wspace=0.05)

ax[0].bar(bins[:-1], Y, width=1, ec='k') # Grafico el histograma (grafico de barras)
ax[1].bar(bins[:-1], Y, width=0.5, ec='k')
ax[2].stem(bins[:-1], Y, basefmt=' ', use_line_collection=True) # Stem-plot

for k, a in enumerate(ax, 1):
    a.set_title(k, loc='left', fontsize=20)

plt.show()

#Normalizacion
Y_normed = Y / np.sum(Y)

f, ax = plt.subplots(ncols=3, figsize=(16,4), sharey=True)
f.subplots_adjust(wspace=0.05)

ax[0].bar(bins[:-1], Y_normed, width=1, ec='k')
ax[1].bar(bins[:-1], Y_normed, width=0.5, ec='k')
ax[2].stem(bins[:-1], Y_normed, basefmt=' ', use_line_collection=True)

for k, a in enumerate(ax, 1):
    a.scatter(bins[:-1], X.pmf(bins[:-1]), color='red', zorder=3)
    a.set_title(k, loc='left', fontsize=20)

plt.show()