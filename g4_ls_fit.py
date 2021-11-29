#https://python4mpia.github.io/fitting_data/least-squares-fitting.html
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization

from scipy.optimize import curve_fit

# Generate artificial data = straight line with a=0 and b=1
# plus some noise.
#xdata = np.array([0.0,1.0,2.0,3.0,4.0,5.0])
#ydata = np.array([0.1,0.9,2.2,2.8,3.9,5.1])
#sigma = np.array([1.0,1.0,1.0,1.0,1.0,1.0])

def func(x, a, b, c):
    return a + b*x + c*x*x

#Frodesen example 10.2.5
xdata = np.array([-0.6,-0.2,0.2,0.6])
ydata = np.array([5,3,5,8])
sigma = np.array([2,1,1,2])

# Initial guess.
x0    = np.array([1.0, 2.0, 3.0])

xvals = np.arange(-0.6, 0.6, 0.01)

popt, pcov = curve_fit(func, xdata, ydata, x0, sigma,  method='lm',absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))

print(popt)
print(pcov)
print(perr)

plt.errorbar(xdata, ydata, yerr=sigma, fmt='.k',label='data')
plt.plot(xvals, func(xvals, *popt), 'g--',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
