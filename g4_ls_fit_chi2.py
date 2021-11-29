import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization

from scipy.optimize import curve_fit

def func(x, a, b):
    return a + b*x


#Cowan Fig 7.2 (valores aproximados, similares a los del grÃ¡fico, pero no iguales!)
xdata = np.array([1,2,3,4,5])
ydata = np.array([1.5,2.33,3.24,3.16,4.6])
sigma = np.array([0.33,0.166,0.33,0.36,0.39])

# Initial guess.
x0    = np.array([1.0, 1.0])

xvals = np.arange(0.0, 6.0, 0.1)

popt, pcov = curve_fit(func, xdata, ydata, x0, sigma,  method='lm',absolute_sigma=True)

perr = np.sqrt(np.diag(pcov))

print(popt)
print(pcov)
print(perr)

plt.errorbar(xdata, ydata, yerr=sigma, fmt='.k',label='data')
plt.plot(xvals, func(xvals, *popt), 'g--',label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


def chi2(y_measure,y_predict,errors):
    """Calculate the chi squared value given a measurement with errors and prediction"""
    return np.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    """Calculate the reduced chi squared value given a measurement with errors and prediction,
    and knowing the number of parameters in the model."""
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)

chi2i  = chi2(ydata, func(xdata, *popt), sigma)
chi2ri = chi2reduced(ydata, func(xdata, *popt), sigma,2)

print("chi2 = ",chi2i)
print("chi2r = ",chi2ri)

from scipy.stats import chi2
#print(1 - chi2.cdf(3.99,3))
print(1 - chi2.cdf(chi2i,3))
