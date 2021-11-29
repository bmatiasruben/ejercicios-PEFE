import scipy.stats as stats
import math

x = 5 # Quiero ver menos de x = 5 en ese período

mean_wt = 15.7 * 0.5 # Caen a 15 por hora, y mido por 3 minutos

sd_wt = math.sqrt(15.7 * 0.5)

prob=stats.norm.cdf((x - mean_wt) / sd_wt)

print('Probabilidad {:.2f}%'.format(prob * 100))
