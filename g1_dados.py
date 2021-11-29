#I created an array filled with 0 with the Numpy function zeros().
#(from https://hadrienj.github.io/posts/Probability-Mass-and-Density-Functions/)
#At each throw, I chose a value among the 6 possibilities.
#Then, I used the Numpy function unique() with the parameter return_counts set to True to get the number of each possible outcome.
#I plotted the proportion for each possible value.

import numpy as np
import matplotlib.pyplot as plt

num_throws = 100000
outcomes = np.zeros(num_throws)
for i in range(num_throws):
   # let's roll the dice
   outcome = np.random.choice(['1', '2', '3', '4', '5', '6'])
   outcomes[i] = outcome

val, cnt = np.unique(outcomes, return_counts=True)
prop = cnt / len(outcomes)

# Now that we have rolled our dice several times, let's plot the results
plt.bar(val, prop)
plt.ylabel("Probability")
plt.xlabel("Outcome")
plt.show()
plt.close()