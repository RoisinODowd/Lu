import sys

if len(sys.argv) != 5:
	sys.stderr.write("The proper usage of this program is 'python reducer.py [MUTATIONS] [EXPRESSIONS (IlluminaHiSeq)] [CNA] [OutputFile]'\n")
	sys.exit()

#1st argument: mutation
#2nd: expression
#3rd: cna
#4th: output file

mutFile = open(sys.argv[1], "r")
expFile = open(sys.argv[2], "r")
cnaFile = open(sys.argv[3], "r")
mutList = mutFile.readline().strip().split("\t")
expList = expFile.readline().strip().split("\t")
cnaList = cnaFile.readline().strip().split("\t")

mutSet = set(mutList)
expSet = set(expList)
cnaSet = set(cnaList)

commonSet = mutSet.intersection(expSet).intersection(cnaSet)
#print len(commonSet)

with open(sys.argv[4], "w") as out:
	#out.write(str(mutSet.intersection(expSet)))
	while len(commonSet) > 0:
		temp = commonSet.pop()
		if temp == "Sample":
			continue
		else:
			out.write(temp + "\n")