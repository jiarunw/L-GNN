import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

im1 = plt.imread('results/test_disp1.jpg')
im2 = plt.imread('results/test_disp8.jpg')
im3 = plt.imread('results/test_disp15.jpg')
im4 = plt.imread('results/test_disp22.jpg')
im5 = plt.imread('results/test_disp29.jpg')
im6 = plt.imread('results/test_disp36.jpg')

fig, ax= plt.subplots(nrows=3, ncols=2,
                                    figsize=(12, 12))

ax[0, 0].set_title('Epoch1')
ax[0, 0].imshow(im1)

ax[1, 0].set_title('Epoch8')
ax[1, 0].imshow(im2)

ax[2, 0].set_title('Epoch15')
ax[2, 0].imshow(im3)

ax[0, 1].set_title('Epoch22')
ax[0, 1].imshow(im4)

ax[1, 1].set_title('Epoch29')
ax[1, 1].imshow(im5)

ax[2, 1].set_title('Epoch36')
ax[2, 1].imshow(im6)

for i in range(3):
    for j in range(2):
        ax[i, j].axis('off')
plt.tight_layout()
plt.show()