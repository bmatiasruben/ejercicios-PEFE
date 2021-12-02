#http://users.df.uba.ar/maurosilber/incertezas/histogramas.html
import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt
#matplotlib inline

np.random.seed(42) # Para obtener la misma secuencia de numeros aleatorios cada vez que lo ejecuto
X = poisson(mu=4.5) # Defino una variable aleatoria con distribucion de Poisson de parametro mu=4.5
Xi = X.rvs(size=1000) # Genero 1000 numeros de la variable aleatoria

Y, bins = np.histogram(Xi, bins=np.arange(0, Xi.max())) # Genero el histograma de 0 a 10

f, ax = plt.subplots(ncols=3, figsize=(16,4), sharey=True) # Share Y hace que compartan eje Y
f.subplots_adjust(wspace=0.05)

# El bins[:-1] me agarra todos los elementos menos el último (porque necesito 10 barras y de 0 a 10 hay 11)
ax[0].bar(bins[:-1], Y, width=1, ec='k') # Grafico el histograma (grafico de barras)
ax[1].bar(bins[:-1], Y, width=0.5, ec='k')
ax[2].stem(bins[:-1], Y, basefmt=' ', use_line_collection=True) # Stem-plot

for k, a in enumerate(ax, 1): # El , 1 hace que arranque en 1 el enumerate
    a.set_title(k, loc='center', fontsize=20)

plt.show()

#Normalizacion
Y_normed = Y / np.sum(Y) # Normaliza, no hay mucha ciencia acá 

f, ax = plt.subplots(ncols=3, figsize=(16,4), sharey=True)
f.subplots_adjust(wspace=0.05)

ax[0].bar(bins[:-1], Y_normed, width=1, ec='k')
ax[1].bar(bins[:-1], Y_normed, width=0.5, ec='k')
ax[2].stem(bins[:-1], Y_normed, basefmt=' ', use_line_collection=True)

# Ploteo un scatter de lo esperado para cada media
for k, a in enumerate(ax, 1):
    a.scatter(bins[:-1], X.pmf(bins[:-1]), color='red', zorder=3) 
    # El Z Order me modifica para que aparezca arriba el scatter
    a.set_title(k, loc='center', fontsize=20)

plt.show()