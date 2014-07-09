#All matrices are non-transposed

import numpy as np
import sys
from scipy.stats import norm

if len(sys.argv) != 3:
	sys.stderr.write("The proper usage of this program is 'python cdfMaker.py [NormalMatrix] [TumorMatrix] [OutputFile]'\n")
	sys.exit()

def strip_first_col(fname, delimiter=None):
    with open(fname, 'r') as fin:
        for line in fin:
            try:
               yield line.split(delimiter, 1)[1]
            except IndexError:
               continue

def getStats(fileName):
	data = np.loadtxt(strip_first_col(fileName), skiprows=1)
	return (data.mean(axis=0), data.std(axis=0))

cdfMat = [[]]

normalFilePath = sys.argv[1]
tumorFile = sys.argv[2]

meanSTDTuple = getStats(normalFilePath)
tumorMatrix = np.loadtxt(strip_first_col(tumorFile), skiprows=1)



for line in tumorMatrix:
 	tempList = []

 	for i in range(0, len(line)):
 		tempList.append(norm.cdf(line[i], meanSTDTuple[0][i], meanSTDTuple[1][i]))

	cdfMat.append(tempList)

with open(sys.argv[2], "w") as out:
	for line in cdfMat:
		for i in line:
			out.write(str(i) + "\t")

		out.write("\n")

out.close()