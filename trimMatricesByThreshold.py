#MAKE SURE MATRIX IS GENES x TUMORS

import sys

cancerMatrix = open(sys.argv[1], "r")
trimmedMatrix = open(sys.argv[2], "w")

threshold = 0.02
trimmedMatrix.write(cancerMatrix.readline())

for line in cancerMatrix:
	curLine = line.strip().split("\t")
	numOnes = 0
	for i in range(1, len(curLine)):
		if curLine[i] == "1":
			numOnes += 1
	if numOnes / float(len(curLine) - 1) > threshold:
		trimmedMatrix.write(line)

cancerMatrix.close()
trimmedMatrix.close()



# copyMatrix = []

# for line in cancerMatrix:
# 	copyMatrix.append(line.strip().split("\t"))


# for i in range(1: len(copyMatrix[0])):
# 	countOnes = 0
# 	for j in range(1: len(copyMatrix)):
# 		if copyMatrix[j][i] == "1":
# 			countOnes += 1

		