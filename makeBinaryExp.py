import sys
import numpy as np

ALPHA = 0.001

data = np.loadtxt(sys.argv[1], skiprows=1)
newData = np.zeros(data.shape)

newData[data < ALPHA] = 1
newData[1 - data < ALPHA] = 1

newData = np.int32(newData)

np.savetxt(sys.argv[2], newData, delimiter ='\t', fmt='%d')
