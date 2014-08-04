import sys

"""
Read in Mutation and DEG files. Be sure that both files contain only common tumors between them.
"""

inMutDEGFile1 = open(sys.argv[1], "r")
inMutDEGFile2 = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

"""
Create a list to be populated with tumors
Read and store list of genes from both the mutation file and the DEG file
"""

fileOneGenes = inMutDEGFile1.readline().strip().split("\t")[1:]
fileTwoGenes = inMutDEGFile2.readline().strip().split("\t")[1:]

"""
Obtain the union of fileOneGenes and fileTwoGenes and store them
in "unionGenes". This is the gene list used for our output file.
"""
unionGenes = list(set(fileOneGenes).union(set(fileTwoGenes)))

# instantiate a list keep track how many times a gene across tumors
countsForUnionGenes = [0] * len(unionGenes)

#mutDataDict = {}

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
for i in inMutDEGFile1:
	tmp = [0]*len(unionGenes)
	currentLine = i.strip().split("\t")
	tumorName = currentLine[0]
	# find genes with CNA value of 1 in this tumor
	cnaOneIndex =  [i for i, x in enumerate(currentLine[1:]) if x == "1"]
	cnaGenesWithOne = [fileOneGenes[i] for i in cnaOneIndex] 
	#print cnaOneIndex
	#sys.exit()
	for gene in cnaGenesWithOne:
		tmp[unionGenes.index(gene)] = 1

	#out put the unified data to file
	out.write(tumorName)
	for x in tmp:
		out.write("\t" + str(x))
	out.write("\n")

for i in inMutDEGFile2:
	tmp = [0]*len(unionGenes)

	currentLine = i.strip().split("\t")
	tumorName = currentLine[0]
	# find genes with CNA value of 1 in this tumor
	cnaOneIndex =  [i for i, x in enumerate(currentLine[1:]) if x == "1"]
	cnaGenesWithOne = [fileTwoGenes[i] for i in cnaOneIndex] 
	#print cnaOneIndex
	#sys.exit()
	for gene in cnaGenesWithOne:
		tmp[unionGenes.index(gene)] = 1

	#out put the unified data to file
	out.write(tumorName)
	for x in tmp:
		out.write("\t" + str(x))
	out.write("\n")

