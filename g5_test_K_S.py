#https://www.cienciadedatos.net/documentos/pystats08-comparacion-distribuciones-test-kolmogorov-smirnov-python.html

# Tratamiento de datos
# ==============================================================================
import numpy as np
import pandas as pd

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use('fivethirtyeight')
import seaborn as sns

# Modelado y test estadÃ­sticos
# ==============================================================================
from statsmodels.distributions.empirical_distribution import ECDF
from scipy.stats import ks_2samp

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# Datos
# ==============================================================================
url = ('https://raw.githubusercontent.com/JoaquinAmatRodrigo/'
       'Estadistica-machine-learning-python/master/data/Snmesp.csv')
datos = pd.read_csv(url)
datos['year'] = datos['year'].astype(str) 
datos.info()

# Gráficos distribución observada
# ==============================================================================
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(7, 6))
sns.violinplot(
    x     = datos.salary,
    y     = datos.year,
    color = ".8",
    ax    = axs[0]
)

sns.stripplot(
    x     = datos.salary,
    y     = datos.year,
    data = datos,
    size = 4,
    jitter  = 0.1,
    ax = axs[0]
)
axs[0].set_title('DistribuciÃ³n de salarios por aÃ±o')
axs[0].set_ylabel('aÃ±o')
axs[0].set_xlabel('salario');

for year in datos.year.unique():
    datos_temp = datos[datos.year == year]['salary']
    datos_temp.plot.kde(ax=axs[1], label=year)
    axs[1].plot(datos_temp, np.full_like(datos_temp, 0), '|k', markeredgewidth=1)

#axs[1].set_xlabel('aÃ±o');
axs[1].set_xlabel('salario');
axs[1].legend()

fig.tight_layout();

plt.show()


# Ajuste de las funciones ecdf con cada muestra
# ==============================================================================
ecdf_1989 = ECDF(datos.loc[datos.year == '1989', 'salary'])
ecdf_1990 = ECDF(datos.loc[datos.year == '1990', 'salary'])

# EstimaciÃ³n de la probabilidad acumulada de cada valor de salario observado
# ==============================================================================
grid_salario = np.sort(datos.salary.unique())
prob_acumulada_ecdf_1989 = ecdf_1989(grid_salario)
prob_acumulada_ecdf_1990 = ecdf_1990(grid_salario)


# RepresentaciÃ³n grÃ¡fica de las curvas ecdf
# ==============================================================================
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))
ax.plot(grid_salario, prob_acumulada_ecdf_1989, label='1989')
ax.plot(grid_salario, prob_acumulada_ecdf_1990, label='1990')
ax.set_title("FunciÃ³n de distribuciÃ³n acumulada empÃ­rica salarios")
ax.set_ylabel("Probabilidad acumulada")
ax.legend();

plt.show()

# RepresentaciÃ³n grÃ¡fica de las curvas ecdf
# ==============================================================================
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))
# sns.ecdfplot(data=datos, x="salary", hue='year', ax=ax)
# ax.set_title("FunciÃ³n de distribuciÃ³n acumulada empÃ­rica salarios")
# ax.set_ylabel("Probabilidad acumulada");

# Distancia Kolmogorovâ€“Smirnov
# ==============================================================================
abs_dif = np.abs(prob_acumulada_ecdf_1989 - prob_acumulada_ecdf_1990)
distancia_ks = np.max(abs_dif)
print(f"Distancia Kolmogorovâ€“Smirnov: {distancia_ks :.4f}")

plt.show()

# Test Kolmogorovâ€“Smirnov entre dos muestras
# ==============================================================================
KS_testResult = ks_2samp(
    datos.loc[datos.year == '1989', 'salary'],
    datos.loc[datos.year == '1990', 'salary']
)

print(KS_testResult)