#https://datatofish.com/covariance-matrix-python/
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

arrayA = [45,37,42,35,39] # Llamar las cosas con una sola letra no me gusta
arrayB = [38,31,26,28,33]
arrayC = [10,15,17,21,12]

data = np.array([arrayA,arrayB,arrayC]) # Junto los tres arrays en un array grande

covMatrix = np.cov(data,bias=False) # Determino la matriz de covarianza
print (covMatrix)

sn.heatmap(covMatrix, annot=True, fmt='g')
plt.show()

# Pandas only version
import pandas as pd
data = {'A': [45,37,42,35,39],
       'B': [38,31,26,28,33],
       'C': [10,15,17,21,12]
       }
df = pd.DataFrame(data,columns=['A','B','C'])
covMatrix = pd.DataFrame.cov(df)
print (covMatrix)

