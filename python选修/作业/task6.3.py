import matplotlib.pyplot as plt
labels = 'python','c++','scala','java','php','vhdl'
sizes = 15,20,30,15,10,20
colors = 'yellowgreen','gold','lightskyblue','lightcoral','purple','pink'
explode = 0.1,0,0,0,0,0
plt.pie(sizes,explode = explode,labels = labels,colors = colors,autopct = '%2.3f%%',shadow = True,startangle = 50)
plt.axis('equal')
plt.show()
