import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data = {'A': [45,37,42,35,39],
        'B': [38,31,26,28,33],
        'C': [10,15,17,21,12]
        }

df = pd.DataFrame(data,columns=['A','B','C'])
print (df)

corrMatrix = df.corr() # Idem archivo cov.py pero con la matriz de correlaciones
print (corrMatrix)

sn.heatmap(corrMatrix, annot=True)
plt.show()