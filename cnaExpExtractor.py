import sys

cnaMatrixTrans = open(sys.argv[1], "r")
expMatrixTrans = open(sys.argv[2], "r")
comTumorList = open(sys.argv[3], "r")
cnaComMatOut = open(sys.argv[4], "w")
expComMatOut = open(sys.argv[5], "w")

for line in cnaMatrixTrans:
	for line2 in comTumorList:
		if line.split("\t")[0] == line2.strip():
			cnaComMatOut.write(line)
			
for line in expMatrixTrans:
	for line2 in comTumorList:
		if line.split("\t")[0] == line2.strip():
			expComMatOut.write(line)