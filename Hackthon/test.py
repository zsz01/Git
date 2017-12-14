import matplotlib.pyplot as plt
import matplotlib.image as img

dest = img.imread(r'.\template\pict.jpg')
plt.imshow(dest)
plt.axis('off')
plt.show()