#http://materias.df.uba.ar/estadisticaa2017c1/files/2012/07/Poisson_limite_exacto.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Saco los punto y coma porque no es de python 
alpha=0.68

critical_value = (1-alpha)/2
# Innecesario esta asignación
#R = L

k = np.arange(0,12)
a = chi2.ppf(critical_value,2*k)/2 # probabilidad de Poisson x mayor que N es igual a la probabilidad de Chi2 con 2N grados de libertad
b = chi2.ppf(1-critical_value,2*(k+1))/2

print(a)
print(b)

plt.step(k+1, a, label='Lí­mite inferior')
plt.step(k, b, label='Lí­mite superior')
plt.title("Cinturón de confianza")
plt.legend()
plt.grid()
plt.xlim(-0.1, 10)
plt.ylim(-0.1, 14)
plt.show()