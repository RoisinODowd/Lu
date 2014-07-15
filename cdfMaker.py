#All matrices are non-transposed

import numpy as np
import sys
from scipy.stats import norm

###
# Improper argument handling
###
if len(sys.argv) != 3:
	sys.stderr.write("The proper usage of this program is 'python cdfMaker.py [NormalMatrix] [TumorMatrix] [OutputFile]'\n")
	sys.exit()

###
# Strips the entire first column from the file passed to the
# function.
###
def strip_first_col(fname, delimiter=None):
    with open(fname, 'r') as fin:
        for line in fin:
            try:
               yield line.split(delimiter, 1)[1]
            except IndexError:
               continue

###
# Returns a tuple that contains a list of means and list of
# corrected standard deviations for each column in the
# passed file.
#
# ([List of means], [List of standard devations])
###
def getStats(fileName):
	data = np.loadtxt(strip_first_col(fileName), skiprows=1)
	return (data.mean(axis=0), data.std(axis=0, ddof=1))

###
# Declarations
###
cdfMat = [[]]

###
# Pass in two files names, where the first argument is the
# normal matrix (tumor x gene) and the second argument is
# the tumor matrix (tumor x gene).
###
normalFilePath = sys.argv[1]
tumorFile = sys.argv[2]

###
# Get the statistics for the normal matrix via the getStats
# function and load tumorMatrix as a numpy array.
#
# meanSTDTuple = ([List of means], [List of STDs])
# tumorMatrix = np.array                       ]
###
meanSTDTuple = getStats(normalFilePath)
tumorMatrix = np.loadtxt(strip_first_col(tumorFile), skiprows=1)

###
# Go through each element in tumorMatrix and calculate the CDF
# (cumulative density function) for each element and append each
# value to tempList. tempList then contains the CDFs for each
# row in tumorMatrix. tempList is then appended to cdfMat.
#
# tempList = [CDF1, CDF2, ...]
# cdfMat = [[Row1], [Row2], ...]
###
for line in tumorMatrix:
 	tempList = [] #local scope declaration
 	for i in range(0, len(line)):
 		tempList.append(norm.cdf(line[i], meanSTDTuple[0][i], meanSTDTuple[1][i]))
	cdfMat.append(tempList)

###
# Open an output file and write each CDF value on its
# respective row.
###
with open(sys.argv[2], "w") as out:
	for line in cdfMat:
		for i in line:
			out.write(str(i) + "\t")
		out.write("\n")

###
# Closing files
###
out.close()
