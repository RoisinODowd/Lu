import sys

"""
Improper argument handling
"""
if len(sys.argv) != 4:
	sys.stderr.write("The proper usage of this program is 'python makeSuperset.py [BinaryCDFWithHeaders] [CNA] [OutputFile]'\n")
	sys.exit()

"""
Open three files. Two matrices, the binary CDFs and
the CNA matrix that are tumor x gene with row
and column headers, and an output file.
"""
cdfFile = open(sys.argv[1], "r")
cnaFile = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

"""
Declarations
"""
cdfTumorDict, cdfGeneDict = {}, {}
cnaTumorDict, cnaGeneDict = {}, {}
cdfGeneList, cnaGeneList, tumorList = [], [], []


"""
Read in the header of both files, which is all the genes,
and then put all the genes into their respective lists.
Then, remove the non-gene headers from both lists, and
then make a commonGeneList which is the intersection of
both cdfGeneList and cnaGeneList.

cdfGeneList = ['Gene1', 'Gene2', 'Gene4', ...]
cnaGeneList = ['Gene1', 'Gene3', 'Gene4', ...]
commonGeneList = ['Gene1', 'Gene4', ...]
"""
cdfGeneList = cdfFile.readline().strip().split("\t")
cnaGeneList = cnaFile.readline().strip().split("\t")
cdfGeneList.remove("sample")
cnaGeneList.remove("Gene Symbol")
commonGeneList = list(set(cdfGeneList).intersection(set(cnaGeneList)))

"""
For each element in the commonGeneList, store that gene in two
dictionaries where the key is the gene and the value is the index
of that gene in either the cdfGeneList or cnaGeneList.

cdfGeneDict = {'Gene1': intIndex, 'Gene2': intIndex, ...}
cnaGeneDict = {'Gene1': intIndex, 'Gene2': intIndex, ...}
"""
counter = 0
for i in commonGeneList:
	cdfGeneDict[i] = cdfGeneList.index(i)
counter = 0
for i in commonGeneList:
	cnaGeneDict[i] = cnaGeneList.index(i)

"""
Set the files back to that start.
"""
cdfFile.seek(0)
cnaFile.seek(0)

"""
Go through each line in both cdfFile and cnaFile. Add each TCGA id
to a dictionary as a key and the rest of the line as its value.
Then, remove the non-TCGA headers from the dictionaries.

cdfTumorDict = {"TCGA1": "Line", "TCGA2": "Line", ...}
cnaTumorDict = {"TCGA1": "Line", "TCGA2": "Line", ...}
"""
for line in cdfFile:
	cdfTumorDict[line.split("\t")[0]] = line.strip().split("\t")
for line in cnaFile:
	cnaTumorDict[line.split("\t")[0]] = line.strip().split("\t")
cdfTumorDict.pop("sample")
cnaTumorDict.pop("Gene Symbol")

"""
Go through each tumor in cnaTumorDict. Each tumor is appended to
tumorList to be written as a row header later. tumorDEGList is
created as a list of len(commonGeneList) zeroes. For each gene in
commonGeneList, the index of that gene is found in both the cdfLine
and the cnaLine. Those two values are then checked to see if that
gene is differentially expressed within that tumor, and if it is,
a 1 is written in the ith index, where i is the location of the gene
in commonGeneList. Each tumor is its own list.

degList = [[0,1,0,...], [0,1,0,...], ...]
tumorList = ['TCGAId', 'TCGAId', ...]
tumorDEGList = [0,0,0,0,0...len(commonGeneList)]
cnaLine = [-1, -2, 1, 2,...]
cdfLine = [0, 1, 1, 0, ...]
"""
degList = []
count = 0
for i in cnaTumorDict:
	tumorList.append(i)
	tumorDEGList = [0] * len(commonGeneList)
	cnaLine = cnaTumorDict[i]
	cdfLine = cdfTumorDict[i]
	for gene in commonGeneList:
		cdfIndex = cdfGeneDict[gene]
		cnaIndex = cnaGeneDict[gene]
		if abs(int(cnaLine[cnaIndex+1])) == 2 and int(cdfLine[cdfIndex+1]) == 1:
			tumorDEGList[commonGeneList.index(gene)] = 1
			count += 1
	degList.append(tumorDEGList)

"""
Write out the genes as the first row for column headers, and
the tumors along with their corresponding data as the other lines.
"""
out.write("sample\t")
for i in commonGeneList:
	out.write(i + "\t")
out.write("\n")
for i in range(len(degList)):
	out.write(str(tumorList[i]) + "\t")
	for j in degList[i]:
		out.write(str(j) + "\t")
	out.write("\n")
print count