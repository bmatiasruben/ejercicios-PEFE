#http://eric.univ-lyon2.fr/~ricco/tanagra/fichiers/en_Tanagra_Calcul_P_Value.pdf
import numpy as np # Pa que si no lo estoy ni usando??
import matplotlib.pyplot as plt # Idem numpy
import scipy.stats as stats

from scipy.stats import chi2

from scipy.stats import poisson

#p value of poisson probability to have >=5 events with mu=2.55 
print(poisson.sf(4, 2.55))

#CDF of the standard normal distribution (Î¼ = 0 and Ïƒ = 1). Probability of less than x = 1.65 
print(stats.norm.cdf(1.65, loc = 0, scale = 1))

#Calculation of the p-value for the standard normal distribution in a right tailed test. The probability of more than z = 2.1
#1 - stats.norm.cdf(2.1)
print(stats.norm.sf(2.1))

#Calculation of the p-value for the standard normal distribution in a two- tailed test. The probability of more than z = 2.1 in absolute value
print(2 * (1 - stats.norm.cdf(2.1)))

#PPF (q) of the standard normal distribution for the probability (1 â€“ Î±) = 0.95
print(stats.norm.ppf(0.95, loc = 0, scale = 1))

#CDF of Studentâ€™s t-distribution with k (k > 0) degrees of freedom. Probability of less than t = 1.5 with k = 10.
print(stats.t.cdf(1.5, df = 10))

#PPF (q) of the Studentâ€™s t-distribution with k = 10 degrees of freedom for the probability (1 â€“ Î±) = 0.95
print(stats.t.ppf(0.95, df = 10))

#CDF of the CHI-SQUARED distribution with k (k > 0) degrees of freedom. Probability of less than t = 12.0 with k = 5.
print(chi2.cdf(12.0, df = 5))

#PPF (q) of the chi-squared distribution with k = 7 degrees of freedom for the probability (1 â€“ Î±) = 0.95
print(chi2.ppf(0.95, df = 7))
