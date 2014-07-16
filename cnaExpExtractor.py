import sys

cnaMatrixTrans = open(sys.argv[1], "r")
expMatrixTrans = open(sys.argv[2], "r")
comTumorList = open(sys.argv[3], "r")
cnaComMatOut = open(sys.argv[4], "w")
expComMatOut = open(sys.argv[5], "w")

cnaDict = {}
expDict = {}

header = cnaMatrixTrans.readline()
next(expMatrixTrans)
cnaComMatOut.write(header)
expComMatOut.write(header)

for line in cnaMatrixTrans:
	cnaDict[str(line.split("\t")[0])] = str(line[15:])

for line in expMatrixTrans:
	expDict[str(line.split("\t")[0])] = str(line[15:])

for line in comTumorList:
	if line.strip() in cnaDict and line.strip() in expDict:
		cnaComMatOut.write(line.strip() + cnaDict[str(line.strip())])

comTumorList.seek(0)

for line in comTumorList:
	if line.strip() in expDict and line.strip() in cnaDict:
		expComMatOut.write(line.strip() + expDict[str(line.strip())])
		
cnaComMatOut.close()
expComMatOut.close()
