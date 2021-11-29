# C:\Users\Mati\AppData\Local\Programs\Virtualenv\Scripts\activate.ps1 usar esto para habilitar python 3.8
#http://www.pp.rhul.ac.uk/~cowan/stat/root/expFit/python/expFit.py

import numpy as np
import scipy.stats as stats
from iminuit import Minuit
import matplotlib.pyplot as plt

# Generate the data
xi = 1.0 # Defino la media
num_samples = 200 # 200 muestras

def transform(r): # El argumento está para poder generar el vector más adelante. Medio incomodo, podría hacerse de otra manera
    return np.random.exponential(scale=xi) # Genero un número aleatorio siguiendo una distribución exponencial con media xi=1

uni = np.random.rand(num_samples)

# Le paso como argumento a la función un vector de longitud num_samples
# para generar un vector de esa longitud pero con distribución exponencial
data = np.vectorize(transform)(uni) 

# Define the negative log-likelihood (negative so as to minimize)

def negLogL(p1):
    pdf = stats.expon.pdf(data, scale=p1)
    if np.any(np.isnan(pdf)) or np.any(pdf <= 0): # Pregunta si algún número es infinito o menor o igual que 0
        return 9e99 # Minuit doesn't like np.nan
    return -np.sum(np.log(pdf))

# Do the fit
params = {'p1':1.5, 'error_p1':0.1}                  # guess initial values
minuit = Minuit(negLogL, errordef=0.5, **params)     # gets errors from lnL = lnLmax - 0.5
migrad = minuit.migrad()

# Covariance matrix
#minuit.covariance

# Make a plot

fig = plt.figure(figsize=(8,6))

# Histogram
plt.hist(data, bins=50, density=True, alpha=.5)

# Fit pdf
xvals = np.linspace(0, 25, 200)
p1 = minuit.args
yvals = [stats.expon.pdf(x, scale=p1) for x in xvals]
plt.plot(xvals, yvals)

# Sample ticks
tick_height = 0.05
xvals = [data, data]
yvals = [np.zeros_like(data), tick_height * np.ones_like(data)]
plt.plot(xvals, yvals, color='black', linewidth=1)

plt.xlabel('x')
plt.ylabel(r'$f(x;\xi)$')
plt.xlim(0, 5)
plt.ylim(0, None)
plt.show()
