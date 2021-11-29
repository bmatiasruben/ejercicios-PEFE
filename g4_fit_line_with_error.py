#Parcialmente basado en https://micropore.wordpress.com/2017/02/04/python-fit-with-error-on-y-axis/
#%%
import numpy as np
from pylab import *
from scipy.optimize import curve_fit
from matplotlib import rcParams

def func(x, a, b):

    return a + b * x 

# test data and error

x1=0.
x2=1.
nBins=10
sigma = 0.2
mean  = 0.

x = np.linspace(x1, x2, nBins)

y0 = 2. + 3.*x

noise = np.random.normal(mean, sigma, len(x))

y = y0 + noise

# curve fit [with only y-error]
popt, pcov = curve_fit(func, x, y)
perr = np.sqrt(np.diag(pcov))

#print fit parameters and 1-sigma estimates
print('fit parameter 1-sigma error')
print('â€”â€”â€”â€”â€”â€”â€”â€”â€”â€”â€”â€“')
for i in range(len(popt)):
    print(str(popt[i])+' +- '+str(perr[i]))


print(pcov)

Va = pcov[0][0]
Vb = pcov[1][1]
Vab = pcov[1][0]

dfda = 1.
dfdb = x

variance = np.power(dfda,2)*Va + np.power(dfdb,2)*Vb + 2.*dfda*dfdb*Vab;

# prepare confidence level curves
nstd = 2. # to draw nstd-sigma intervals

#Propuesta 1
popt_up = popt + nstd * perr
popt_dw = popt - nstd * perr

fit = func(x, *popt)
fit_up = func(x, *popt_up)
fit_dw = func(x, *popt_dw)

#Propuesta 2
fit_cov_up = fit + nstd*np.sqrt(variance)
fit_cov_dw = fit - nstd*np.sqrt(variance)

#Propuesta 3
variance_no_cov = np.power(dfda,2)*Va + np.power(dfdb,2)*Vb
fit_no_cov_up = fit + nstd*np.sqrt(variance_no_cov)
fit_no_cov_dw = fit - nstd*np.sqrt(variance_no_cov)

#plot
fig, ax  = plt.subplots(1)

rcParams['xtick.labelsize'] = 18
rcParams['ytick.labelsize'] = 18
rcParams['font.size']= 20
errorbar(x, y0, yerr=noise, xerr=0, ecolor='k', fmt='none', label='data')

xlabel('x', fontsize=18)
ylabel('y', fontsize=18)
title('fit with only Y-error', fontsize=18)
plot(x, fit, 'r', lw=2, label='best fit curve')
plot(x, y0, 'k', lw=2, label='True curve')
#ax.fill_between(x, fit_up, fit_dw, alpha=.25, label='2-sigma interval simple param')
# ax.fill_between(x, fit_no_cov_up, fit_no_cov_dw, alpha=.45, label='2-sigma interval no cov')
ax.fill_between(x, fit_cov_up, fit_cov_dw, alpha=.65, label='2-sigma interval with cov')

legend(loc='upper left',fontsize=8)
show()
