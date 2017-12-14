import matplotlib.pyplot as plt
import math
delta=2*math.pi/100
x=[i*delta for i in range(101)]
y=[math.sin(i) for i in x]
plt.plot(x,y)
plt.show()
