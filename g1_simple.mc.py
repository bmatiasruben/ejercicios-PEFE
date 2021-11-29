# Simple Monte Carlo program to make histogram of uniformly distributed random values and plot
# G. Cowan, RHUL Physics

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Generate data and store in numpy array, put into histogram

numVal = 10000
nBins = 100
xMin = 0.
xMax = 1.
xData = np.random.uniform(xMin, xMax, numVal)
xHist, bin_edges = np.histogram(xData, bins=nBins, range=(xMin, xMax))

# Make plot and save in file

binLo, binHi = bin_edges[:-1], bin_edges[1:]
xPlot = np.array([binLo, binHi]).T.flatten()
yPlot = np.array([xHist, xHist]).T.flatten()
fig, ax = plt.subplots(1,1)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.set_xlim((xMin, xMax))
ax.set_ylim((0., 150))
plt.xlabel(r'$x$', labelpad=0)
plt.plot(xPlot, yPlot)
#plt.show()
plt.savefig("uniformHist.png", format='png')