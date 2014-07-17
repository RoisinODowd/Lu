import sys

mutFile = open(sys.argv[1], "r")
degFile = open(sys.argv[2], "r")

mutTumors = []
degTumors = []
mutGenes = mutFile.readline().strip().split("\t")
degGenes = degFile.readline().strip().split("\t")
mutLookupDict, degLookupDict = {}, {}

unionGenes = list(set(mutGenes).union(set(degGenes)))

"""
Popualte dictionary
"""

for i in mutFile:
	currentLine = i.strip().split("\t")
	tumorName = currentLine[0]
	for g in range(1, currentLine):
		mutLookupDict[(tumorName, mutGenes[g])] = str(currentLine[g])

print mutLookupDict
