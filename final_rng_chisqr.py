import random
import matplotlib.pyplot as plt
import scipy.stats 
import numpy as np
from collections import Counter

random.seed(651997)

number_amount = [100, 10000, 1000000]
chisqr_results = []

for number in number_amount:
    random_list = [random.randint(1,256) for i in range(number)]
    random_dict = Counter(random_list)
    random_hist = [number_in for number_in in list(random_dict.values())] 
    chisqr_results.append(scipy.stats.chisquare(random_hist))

x_data = np.arange(1,257)

plt.scatter(x_data, random_hist)
plt.plot(x_data, [1000000/256]*256, color = 'red')
plt.show()

#%%
import random
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import chisquare
import numpy as np
from collections import Counter

j_list = []
for k in range(1000):
    random_list = [random.randint(1,16777216) for i in range(1024)]
    random_ord = sorted(random_list)
    dif_list = []
    for i in range(1023):
        dif_list.append(random_ord[i+1] - random_ord[i])
    dif_dict = dict(Counter(dif_list))
    j=0
    for i in list(set(dif_list)):
        if dif_dict.get(i) > 1:
            j += 1
    j_list.append(j)

j_counts = Counter(j_list)
j_hist = [j_counts[i] for i in sorted(Counter(j_list))]
x_data = sorted(list(j_counts.keys()))
y_data = poisson.pmf(x_data, mu=16)
y_data = [i*1000/sum(y_data) for i in y_data]
print(chisquare(j_hist, y_data))

plt.hist(j_list, bins=25)
plt.plot(x_data,y_data)
plt.show()

#%%
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import chisquare
import numpy as np
from collections import Counter

matrixArray = np.loadtxt('D:\\Archivos\\Documents\\Universidad\\Beca CONICET\\Proyecto doctorado\\QRNG\\matrixList.txt')

j_list = []
for k in range(1000):
    random_list = [int(format(int(matrixArray[3*(i+1024*k)]), '08b')+format(int(matrixArray[3*(i+1024*k)+1]),'08b')+format(int(matrixArray[3*(i+1024*k)+2]),'08b'), 2) for i in range(1024)]
    random_ord = sorted(random_list)
    dif_list = []
    for i in range(1023):
        dif_list.append(random_ord[i+1] - random_ord[i])
    dif_dict = dict(Counter(dif_list))
    j=0
    for i in list(set(dif_list)):
        if dif_dict.get(i) > 1:
            j += 1
    j_list.append(j)

j_counts = Counter(j_list)
j_hist = [j_counts[i] for i in sorted(Counter(j_list))]
x_data = sorted(list(j_counts.keys()))
y_data = poisson.pmf(x_data, mu=16)
y_data = [i*1000/sum(y_data) for i in y_data]
print(chisquare(j_hist, y_data))

plt.hist(j_list, bins=23)
plt.plot(x_data,y_data)
plt.show()