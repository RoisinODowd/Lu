import sys

"""
Read in Mutation and DEG files. Be sure that both files contain only common tumors between them.
"""

mutFile = open(sys.argv[1], "r")
degFile = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

"""
Create a list to be populated with tumors
Read and store list of genes from both the mutation file and the DEG file
"""

mutGenes = mutFile.readline().strip().split("\t")[1:]
degGenes = degFile.readline().strip().split("\t")[1:]

"""
Obtain the union of mutGenes and degGenes and store them
in "unionGenes". This is the gene list used for our output file.
"""
unionGenes = list(set(mutGenes).union(set(degGenes)))

# instantiate a list keep track how many times a gene across tumors
countsForUnionGenes = [0] * len(unionGenes)

mutDataDict = {}

"""
write out the header of the out file
"""
out.write("tumor_samples")
for gene in unionGenes:
	out.write("\t" + gene)
out.write("\n")

"""
Populate dictionary "mutDataDict" in which the keys are the Tumor IDs of the mutation data file 
and the values are the cooresponding mutation data for that tumor.
"""
for i in mutFile:
	currentLine = i.strip().split("\t")
	tumorName = currentLine[0]
	mutDataDict[tumorName] = currentLine[1:]

"""
Go through the DEG file and perform the following algorithm to check for 
"""
tumorsWithMutationsData = mutDataDict.keys()
for i in degFile:
	currentLine = i.strip().split("\t")
	tumorName = currentLine[0]

	# check if current CNA tumor has mutaton data
	if tumorName in tumorsWithMutationsData:
		#prepare to out a combined mutation and CNA data 
		tmp = [0]*len(unionGenes)

		# find genes with CNA value of 1 in this tumor
		cnaOneIndex =  [i for i, x in enumerate(currentLine[1:]) if x == "1"]
		cnaGenesWithOne = [degGenes[i] for i in cnaOneIndex] 
		print cnaOneIndex
		sys.exit()
		for gene in cnaGenesWithOne:
			tmp[unionGenes.index(gene)] = 1
			countsForUnionGenes[unionGenes.index(gene)] += 1

		# find genes with Mut value of 1 in this tumor
		mutOneIndex = [i for i, x in enumerate(mutDataDict[tumorName]) if x == "1"]
		mutGeneWithOne = [mutGenes[i] for i in mutOneIndex]
		for gene in mutGeneWithOne:
			if tmp[unionGenes.index(gene)] == 1:
				countsForUnionGenes[unionGenes.index(gene)] += 1
				continue
			else:
				tmp[unionGenes.index(gene)] = 1

		#out put the unified data to file
		out.write(tumorName)
		for x in tmp:
			out.write("\t" + str(x))
		out.write("\n")



