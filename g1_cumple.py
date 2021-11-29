# Modificando el i_max, cambio hasta cuando quiero calcular las probabilidades
p = 1.0 # Arranca en 1 porque le voy a ir multiplicando cosas
for i in range(1, 100): # Podría arrancar en 2, a 1 le multiplico 365/365 (= 1)
    p = p * (366 - i) / 365
    print ('La probabilidad de que en un grupo de %3d personas, dos cumplan años el mismo dí­a es de %10.6f' % (i, 1-p))

for j in range(1, 19): # Pongo 19 porque quiero llegar hasta 18 alumnos
    pf = (364/365)**j
print ('La probabilidad de que en un grupo de %3d alumnos, alguno cumplan años el mismo dí­a que el docente es %10.6f' % (j, 1-pf))

