import sys

cnaMatrixTrans = open(sys.argv[1], "r")
expMatrixTrans = open(sys.argv[2], "r")
comTumorList = open(sys.argv[3], "r")
cnaComMatOut = open(sys.argv[4], "w")
expComMatOut = open(sys.argv[5], "w")

cnaDict = {}
expDict = {}

for line in cnaMatrixTrans:
	cnaDict[str(line.split("\t")[0])] = str(line.split("\t")[1:])
for line in comTumorList:
	if line.strip() in cnaDict:
		cnaComMatOut.write(line.strip() + "\t" + cnaDict[str(line.strip())]
			
for line in expMatrixTrans:
	expDict[str(line.split("\t")[0])] = str(line.split("\t")[1:])
for line in comTumorList:
	if line.strip() in expDict:
		expComMatOut.write(line.strip() + "\t" + expDict[str(line.strip())]
		
cnaComMatOut.close()
expComMatOut.close()