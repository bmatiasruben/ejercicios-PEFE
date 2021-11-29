import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import math

sns.set(style="darkgrid")

np.random.seed(0)

# Variable X con distribución normal con media 0 y varianza 1/sqrt(pi). Genero 300 datos de eso
x = np.random.normal(0, 1/math.sqrt(math.pi), 300) 

# Variable Y con distribución exponencial con media 1. Genero 300 datos de eso
y = np.random.exponential(1, 300)

g = (sns.jointplot(x, y).set_axis_labels("x", "y"))
#g = (sns.jointplot(x, y).set_axis_labels("x", "y").plot_joint(sns.kdeplot, zorder=0, n_levels=6))

plt.show()