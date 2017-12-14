import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

mu, sigma = 3, 0.6
v = np.random.normal(mu, sigma, 100000)
plt.hist(v,bins = 50, normed = 1, facecolor = 'g')
plt.title('直方图')
plt.text(4,0.5,r'$\mu = 100, \sigma = 15$')
plt.grid(True)
plt.show()
