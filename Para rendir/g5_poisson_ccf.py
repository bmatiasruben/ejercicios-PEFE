#http://materias.df.uba.ar/estadisticaa2017c1/files/2012/07/Poisson_limite_exacto.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2 # Importo la distribución chi² desde scipy

# Saco los punto y coma porque no es de python 
alpha = 0.68 # Defino el porcentaje de confianza para la variable

critical_value = (1 - alpha) / 2 
# Innecesario esta asignación. No realmente, es para poner intervalos distintos en R y L
# R = L

k = np.arange(0,12) # Array del 0 al 11
# probabilidad de Poisson x mayor que x_0 con media N es igual a la probabilidad de Chi2 con 2N grados de libertad
# Probabilidad que x sea menor que critical_value para una Chi2 de orden 2k (me devuelve el u_alpha)
a = chi2.ppf(critical_value,2*k)/2 # Veo la probabilidad de tener Poisson mayor que 0,1,2...,11 con lo que dije arriba
# Probabilidad que x sea menor que 1-critical_value para una Chi2 de orden 2k (me devuelve el v_beta)
b = chi2.ppf(1-critical_value,2*(k+1))/2 # Probabilidad de tener Poisson menor que 1,...,12 

print(a)
print(b)

plt.step(k+1, a, label='Lí­mite inferior', color = 'red')
plt.step(k, b, label='Lí­mite superior', color = 'blue')
plt.title("Cinturón de confianza")
plt.legend()
plt.grid()
plt.xlim(-0.1, 10)
plt.ylim(-0.1, 14)
plt.show()