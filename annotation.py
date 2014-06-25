tss = open("tissueSourceSite.txt", "r")
matrix = open("genomicMatrixTrans", "r")
out = open("tumorsAnnotated.txt", "w")
next(matrix)

tumDict = {}

for line in tss:
	tumDict{str(line.strip().split("\t")[1]): list()}
	for line2 in matrix:
		if line.strip().split("\t")[0] == line2.strip().split("\t")[0][5:7]:
			tumDict{str(line.strip().split("\t")[1]): tumDict{str(line.strip().split("\t")[1])}.append(line2.strip().split("\t")[0])}

print tumDict