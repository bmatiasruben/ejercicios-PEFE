import numpy as np
from scipy import stats as st

mu = 4.5*2 # La suma de dos Poisson es una Poisson con media igual a la suma de las medias

pn = 1 # Asumo probabilidad de 100% en primer caso

for n in range(0,12):
	pn = pn - st.poisson.pmf(n, mu=mu) # Voy restandole al 100% la probabilidad de ver n (con n=0,1,...,12) con una media de 12
# El resultado de esto será la probabilidad de ver 12 o más en 2 horas.
print('La probabilidad es:', pn)    

