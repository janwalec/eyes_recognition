import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel
from skimage import io
import numpy as np


path_closed = "./data/train/Closed_Eyes"
path_open = "./data/train/Open_Eyes"

closed_eyes = os.listdir(path_closed)
open_eyes = os.listdir(path_open)

img = io.imread(path_closed + "/" + closed_eyes[0])

closed_size_array = []
open_size_array = []

for imname in closed_eyes:
    path = path_closed + "/" + imname
    closed_size_array.append(io.imread(path).shape[0])

for imname in open_eyes:
    path = path_open + "/" + imname
    open_size_array.append(io.imread(path).shape[0])



plt.plot(closed_size_array, 'b.')
plt.axis((0, 2000, 55, 185))
plt.savefig("closed.png")
plt.close()

plt.plot(open_size_array, 'r.')
plt.axis((0, 2000, 55, 185))
plt.savefig("open.png")
plt.close()

plt.plot(closed_size_array, 'b.')
plt.axis((0, 2000, 55, 185))
plt.plot(open_size_array, 'r.')
plt.savefig("compare.png")
plt.close()


n = 2000
m = 2

num_closed = np.zeros((n, m), dtype=int)
num_closed[:, 0] = np.arange(n)

num_open = np.zeros((n, m), dtype=int)
num_open[:, 0] = np.arange(n)

# count how many pictures of given size is
for i in range(n):
    num_closed[closed_size_array[i]][1] += 1
    num_open[open_size_array[i]][1] += 1


cl_x = []
cl_y = []
o_x = []
o_y = []
for i in range(n):
    if(num_closed[i][1] != 0):
        cl_x.append(i)
        cl_y.append(num_closed[i][1])
    if (num_open[i][1] != 0):
        o_x.append(i)
        o_y.append(num_open[i][1])



plt.plot(cl_x, cl_y, 'b.', label ="closed eyes")
plt.plot(o_x, o_y, 'r.', label="open eyes")
plt.xlabel("size of a picture (x to x pixels)")
plt.ylabel("number of pictures in the set")
plt.legend()
plt.savefig('test.png')
plt.close()


