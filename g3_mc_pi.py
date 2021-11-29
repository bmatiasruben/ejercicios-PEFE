# Ejemplo mÃ©todo MC para determinar el valor de Pi (https://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo) 
import numpy as np
import math


n = 100000

nr = 0

for i in range(n):
	x = np.random.random()
	y = np.random.random()
	r = math.sqrt(x*x + y*y)
	
	if r < 1:
		nr += 1

mc_pi = 4*nr/n 

print("El valor de pi es = ", mc_pi)