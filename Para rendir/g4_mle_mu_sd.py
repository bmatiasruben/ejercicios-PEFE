#https://medium.com/@rrfd/what-is-maximum-likelihood-estimation-examples-in-python-791153818030
#Discuss what are the determined MLE values for Î¸_mu and Î¸_sigma.

import math
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm

#Letâ€™s say our sample is 3, what is the "probability" it comes from a distribution of Î¼ = 3 and Ïƒ = 1?
print (norm.pdf(3, 3, 1))

#What if it came from a distribution with Î¼ = 7 and Ïƒ = 2?
print (norm.pdf(3, 7, 2))

#So if we want to see the probability of 2 and 6 are drawn from a distribution with Î¼ = 4 and Ïƒ = 1 we get:

print (norm.pdf(2, 4, 1)*norm.pdf(6, 4, 1))

# Consider this sample x and letâ€™s compare these values the Likelihood for both PDF ~ N(5, 3) and PDF ~ N(7, 3).
x = [4, 5, 7, 8, 8, 9, 10, 5, 2, 3, 5, 4, 8, 9]

def compare_data_to_dist(x, mu_1=5, mu_2=7, sd_1=3, sd_2=3):
    l_1  = 1.0
    l_2  = 1.0
    ll_1 = 0
    ll_2 = 0
    # Reemplazo los valores iniciales por 1, y cambio las sumas por multiplicaciones 
    # en la definicion del likelihood
    # En el log-likelihood lo dejo como esta
    for i in x:
        l_1  *= norm.pdf(i, mu_1, sd_1)
        l_2  *= norm.pdf(i, mu_2, sd_2)
        ll_1 += np.log(norm.pdf(i, mu_1, sd_1))
        ll_2 += np.log(norm.pdf(i, mu_2, sd_2))

    # Cambio para usar fstrings, queda más cómodo

    print (f"The L of x for mu = {mu_1} and sd = {sd_1} is: {l_1}")
    print (f"The L of x for mu = {mu_2} and sd = {sd_2} is: {l_2}")

    print (f"The LL of x for mu = {mu_1} and sd = {sd_1} is: {ll_1}")
    print (f"The LL of x for mu = {mu_2} and sd = {sd_2} is: {ll_2}")

    # print ("The L of x for mu = %d and sd = %d is: %.4f" % (mu_1, sd_1, l_1))
    # print ("The L of x for mu = %d and sd = %d is: %.4f" % (mu_2, sd_2, l_2))

    # print ("The LL of x for mu = %d and sd = %d is: %.4f" % (mu_1, sd_1, ll_1))
    # print ("The LL of x for mu = %d and sd = %d is: %.4f" % (mu_2, sd_2, ll_2))

# Llamo a la función
compare_data_to_dist(x)

# Plot the Maximum Likelihood Functions for different values of mu and sigma
# Funcion para plotear nomá
def plot_ll(x):
    plt.figure(figsize=(5,8))
    plt.title("Maximim Likelihood Functions")
    plt.xlabel("Mean Estimate")
    plt.ylabel("Log Likelihood")
    plt.ylim(-40, -30)
    plt.xlim(0, 12)
    mu_set = np.linspace(0, 16, 1000)
    #sd_set = [0.5, 1, 1.5, 2.5, 3, 3.5]
    # Seteo otros valores para la desv estandar para plotear el Likelihood
    sd_set = [2.3, 2.35, 2.4, 2.45, 2.5, 2.55]
    max_val = max_val_location = None
    for i in sd_set:
        ll_array = []
        
        for j in mu_set:
            temp_mm = 0
            
            for k in x:
                temp_mm += np.log(norm.pdf(k, j, i)) # The LL function
            ll_array.append(temp_mm)
        
            if (max_val is None):
                max_val = max(ll_array)
            elif max(ll_array) > max_val:
                max_val = max(ll_array)
                max_val_location = j
        
        print (f"The max LL for sd {i} is {max(ll_array)}")    
        # Plot the results
        plt.plot(mu_set, ll_array, label=f"sd: {i}")
        plt.axvline(x=max_val_location, color='black', ls='-.')
        plt.legend(loc='lower left')
        #plt.show()

# Llamo la funcion que me define los plots
plot_ll(x)
# plt.ylim(-170,-32)
# Showeo el plot
plt.show()

#We can use the equations we derived from the first order derivatives above to get those estimates as well:
#Î¸_mu = Î£(x) / n = (2 + 3 + 4 + 5 + 7 + 8 + 9 + 10) / 8 = 6.214 
# Very close to our graph
#Î¸_sigma = Î£(x - Î¸_mu)^2 / n = Î£(x - 6.214)^2 / 8 = 2.425
# Also very close to our graph
# We can also verify these with the standard mean and std functions
# in numpy
print(np.mean(x))
print(np.std(x))

