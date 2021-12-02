# Ejemplo mÃ©todo MC para determinar el valor de Pi (https://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo) 
import numpy as np
import math

# Hago un MonteCarlo de 100000 pasos
n = 100000

# Arranco la cantidad de 'hits' en 0
nr = 0

for i in range(n):
	# Me genero dos números aleatorios x e y, y veo que esten dentro del circulo unidad
	x = np.random.random()
	y = np.random.random()
	r = math.sqrt(x*x + y*y)
	
	# Esto revisa que esté en ese circulo unidad
	if r < 1:
		nr += 1 # Si está, sumo 1 a la cantidad de hits

# Aproximo el area del circulo con nr*4 (porque x e y están entre 0 y 1, es decir el primer cuadrante), 
# y divido por n el area del circulo total
mc_pi = 4*nr/n 

print("El valor de pi es = ", mc_pi)