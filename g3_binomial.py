import numpy as np
from scipy import stats as st

n, p = 10, 0.5

# sumo las probabilidades de obtener 8, 9 y 10 caras en 10 tiradas con n=10 y p=0.5 (definido arriba)
b = st.binom.pmf(8, n=n, p=p) + st.binom.pmf(9, n=n, p=p) + st.binom.pmf(10, n=n, p=p)

print('La probabilidad de mÃ¡s de 7 caras es:', b)

