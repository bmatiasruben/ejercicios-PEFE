import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

np.random.seed(123)
x = np.random.normal(1, 1, 1000)
y = np.random.normal(0, 2, 1000)

sns.distplot(x)
plt.title('x')
plt.xlim(-4, 4)
plt.show()
sns.distplot(y)
plt.title('y')
plt.xlim(-4, 4)
plt.show()