import sys

"""
Improper argument handling
"""
if len(sys.argv) != 6:
	sys.stderr.write("The proper usage of this program is 'python cnaExpExtractor.py [CNA] [EXPRESSIONS] [CommonTumors] [OutputCNA] [OutputExpression]'\n")
	sys.exit()

"""
Open five files, all tumor x gene, the first being the
CNA matrix, the second the expression matrix, the third
the commonTumors list, the fourth the output cnaCommons
matrix, and the fifth the expCommons matrix.
"""
cnaMatrixTrans = open(sys.argv[1], "r")
expMatrixTrans = open(sys.argv[2], "r")
comTumorList = open(sys.argv[3], "r")
cnaComMatOut = open(sys.argv[4], "w")
expComMatOut = open(sys.argv[5], "w")

"""
Declarations
"""
cnaDict = {}
expDict = {}

"""
Read the header from the CNA matrix and the exp Matrix
and output them to the common matrices.

cnaHeader = 'Gene Symbol\tGene1\tGene2...'
expHeader = 'sample\tGene1\tGene2...'
"""
cnaHeader = cnaMatrixTrans.readline()
expHeader = expMatrixTrans.readline()
cnaComMatOut.write(cnaHeader)
expComMatOut.write(expHeader)

"""
Adding values to cnaDict and expDict, where the key is
the TCGA id and the value is the rest of the line.

cnaDict = {"TCGA ID": "Line", "TCGA ID": "Line", ...}
expDict = {"TCGA ID": "Line", "TCGA ID": "Line", ...}
"""
for line in cnaMatrixTrans:
	cnaDict[str(line.split("\t")[0])] = str(line[15:])

for line in expMatrixTrans:
	expDict[str(line.split("\t")[0])] = str(line[15:])

"""
For each line in the commonTumors list, if the id is in
both the cnaDict and expDict, then the whole line is
outputted to cnaComMatOut and expComMatOut.
"""
for line in comTumorList:
	if line.strip() in cnaDict and line.strip() in expDict:
		cnaComMatOut.write(line.strip() + cnaDict[str(line.strip())])

comTumorList.seek(0)

for line in comTumorList:
	if line.strip() in expDict and line.strip() in cnaDict:
		expComMatOut.write(line.strip() + expDict[str(line.strip())])

"""
Closing files
"""
cnaComMatOut.close()
expComMatOut.close()
