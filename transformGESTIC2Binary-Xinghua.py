import sys
out = open(sys.argv[3], "w")

binCDF = open(sys.argv[1], "r")
cnaCommons = open(sys.argv[2], "r")

# load the binary exprs matrix
print "Read in exprs dat"
exprsGeneNames = binCDF.readline().strip().split("\t")[1:]
#print exprsGeneNames 
binMatrix = {}
for line in binCDF:
	tumorId  = line.strip().split("\t")[0]
	values = line.strip().split("\t")[1:]
	binMatrix[tumorId] = values
print "Done"


cnaGeneNames = cnaCommons.readline().strip().split("\t")[1:]
commonGenes = list(set (cnaGeneNames).intersection(set(exprsGeneNames)))

print "There are total " + str(len(commonGenes)) + " common genes from CNA and exprs data"

#print header to out file
out.write("tumor samples")
for geneName in commonGenes:
	out.write("\t" + geneName)
out.write("\n")

print "Processing CNA file"
totalOneWithExprsChange = 0
for line in cnaCommons:
	tmp = [0]*len(commonGenes)
	tumorId = line.strip().split("\t")[0]
	#print "Processing tumor " + tumorId
	if tumorId in binMatrix.keys():
		exprs = binMatrix[tumorId]
	else:
		print "Tumor " + tumorId + "in CNA is not in EXPRS"
		continue

	cnaValues = line.strip().split("\t")[1:]
	cnaOnes = [i for i, x in enumerate (cnaValues) if abs(int(x)) == 2]
	#print "Tumor " + tumorId + " has " + str(len(cnaOnes)) + " copy number altered genes"

	exprs = binMatrix[tumorId]
	#print exprs
	for geneIndex in cnaOnes:
		geneName = cnaGeneNames[geneIndex]
		#print "CNA gene " + geneName + " is altered"
		if geneName in commonGenes:
			if exprs[exprsGeneNames.index(geneName)] == '1':
				tmp[commonGenes.index(geneName)] = 1
				totalOneWithExprsChange += 1
		else:
			#print "CNA gene " + geneName + " is not in the expression"
			pass
	#print "Tumor " + tumorId + " has " + str(sum(tmp)) + " copy number altered genes with differential expression"

	#print out the tmp list with tumorId as CVS
	out.write(tumorId )
	for i in tmp:
		out.write( "\t" + str(i))
	out.write("\n")
print "Total CNA with exprs changes " + str(totalOneWithExprsChange)
out.close()
	