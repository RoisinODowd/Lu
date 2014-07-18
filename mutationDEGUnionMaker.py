import sys

mutFile = open(sys.argv[1], "r")
degFile = open(sys.argv[2], "r")
out = open(sys.argv[3], "r")

tumors = []
outMatrix = []
mutGenes = mutFile.readline().strip().split("\t")
degGenes = degFile.readline().strip().split("\t")
mutLookupDict, degLookupDict = {}, {}

unionGenes = list(set(mutGenes).union(set(degGenes)))

"""
Populate dictionary
"""

for i in mutFile:
	currentLine = i.strip().split("\t")
	tumorName = currentLine[0]
	tumors.append(tumorName)
	for g in range(1, len(currentLine)):
		mutLookupDict[(tumorName, mutGenes[g])] = str(currentLine[g])

for i in degFile:
	currentLine = i.strip().split("\t")
	tumorName = currentLine[0]
	for g in range(1, len(currentLine)):
		degLookupDict[(tumorName, degGenes[g])] = str(currentLine[g])
"""
Populate outMatrix with row and column headers and all zeroes.
"""
temp = [0] * len(unionGenes)
outMatrix.append(["sample"] + unionGenes)
for t in tumors:
	outMatrix.append([t] + temp)

for currLine in outMatrix:
	if currLine[0] == "sample":
		continue
	tumorName = currLine[0]
	for g in range(1,len(currLine)):
		currentGene = unionGenes[g]
		mutValue = 0
		degValue = 0
		if (tumorName, currentGene) in mutLookupDict.keys():
			mutValue = mutLookupDict[(tumorName, currentGene)]
		else:
			mutValue = degLookupDict[(tumorName, currentGene)]
		if (tumorName, currentGene) in degLookupDict.keys():
			degValue = degLookupDict[(tumorName, currentGene)]
		else:
			degValue = mutLookupDict[(tumorName, currentGene)]
		currLine[g] = int(mutValue) | int(degValue)

for i in outMatrix:
	out.write(i)
