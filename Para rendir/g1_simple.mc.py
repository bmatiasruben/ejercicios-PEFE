# Simple Monte Carlo program to make histogram of uniformly distributed random values and plot
# G. Cowan, RHUL Physics

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Generate data and store in numpy array, put into histogram

numVal = 10000 # Cantidad de numeros que genero
nBins = 100 # Defino el numero de bins
xMin = 0. # Entre esto
xMax = 1. # Y esto
xData = np.random.uniform(xMin, xMax, numVal) # Genero el array
xHist, bin_edges = np.histogram(xData, bins=nBins, range=(xMin, xMax)) # genero el histograma con los bins seteados arriba

# Make plot and save in file

binLo, binHi = bin_edges[:-1], bin_edges[1:] # Me genero dos vectores iguales pero corridos un valor
xPlot = np.array([binLo, binHi]).T.flatten() # Me genero una tupla compuesta por los valores inciales y finales de los bins
yPlot = np.array([xHist, xHist]).T.flatten() # Esto hace algo medio rari. 
# Ya lo cacé, agarra los puntos y los une con lineas.
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((xMin, xMax))
ax.set_ylim((0., xHist.max() + 1))
plt.xlabel(r'$x$', labelpad=0) # El r es para latex? eso estaría piola. Ah no, es cursiva nomás 
plt.plot(xPlot, yPlot) 
plt.show()
# plt.savefig("uniformHist.png", format='png')