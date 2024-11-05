import os

from matplotlib import pyplot as plt
from skimage import io
import numpy as np

n = 2000
m = 2

arr = np.zeros((n, m), dtype=int)
arr[:, 0] = np.arange(n)

print(arr)


path_open = "./data/train/Open_Eyes"
open_eyes = os.listdir(path_open)

img = io.imread(path_open + "/" + open_eyes[0])
plt.plot(img, 'r.')
plt.axis((0, 2000, 55, 185))
plt.savefig("open.png")
plt.close()

kernel = [

    [0, -1, 0],
    [0,  5, 0],
    [0, -1, 0]]

