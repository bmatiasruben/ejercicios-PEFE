from numpy import array
from numpy import mean
from numpy import var
from numpy import std
from scipy.stats import skew

# Defino los posibles valores para mi dado
v = array([1,2,3,4,5,6])
print(v)

result_e = mean(v) # Calculo la media de los valores
print(f'Media: {result_e}')

result_v = var(v) # Calculo la varianza de los valores
print(f'Varianza: {result_v}')

result_s = skew(v) # Calculo el skew de los valores
print(f'Skew: {result_s}')


p = array([1/6,1/12,1/12,1/6,3/12,3/12]) # Defino un vector de probabilidades, el elemento i de esto está asociado con el elemento i del dado

# Redefino los dos como 0 para ir sumandole cosas despues
result_e2 = 0
result_v2 = 0

for i in range(len(v)): # Saco el enter porque no me gusta
	result_e2 += v[i]*p[i]

print(result_e2)

for j in range(len(v)): # Idem linea 27
	result_v2 += pow((v[j]-result_e2),2) * p[j]
	
print(result_v2)
