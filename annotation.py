import sys

if len(sys.argv) != 2:
	sys.stderr.write("The proper usage of this program is 'python annotation.py [CommonTumorsFile]'\n")
	sys.exit()


tss = open("./providedFiles/tissueSourceSite.txt", "r")
common = open(sys.argv[1], "r")

tlcSet = set()
tcgaSet = set()
tumDict = {}
mergedList = []
newList = []

for codes in tss:
	twoLetCode = {codes.split("\t")[0]}
	tlcSet.update(twoLetCode)
	mergedList.append([codes.split("\t")[0], codes.split("\t")[2], set()])

for i in range(0, len(mergedList)):
	for j in range(i + 1, len(mergedList)):
		if mergedList[i][1] == mergedList[j][1]:
			temp =  (mergedList[i][1], mergedList[i][2].union(mergedList[j][2]))
			newList.append(temp)
newNewList = []
for i in newList:
	if i not in newNewList:
		newNewList.append(i)

for row in common:
	tcgaId = {row.strip()}
	tcgaSet.update(tcgaId)

while len(tcgaSet) != 0:
	temp = tcgaSet.pop()
	for i in range(0, len(mergedList)):
		if mergedList[i][0] == temp.split("-")[1]:
			for tup in newNewList:
				if mergedList[i][1] == tup[0]:
					tup[1].update({temp})
					
with open("tumorsAnnotated.txt", "w") as out:
	for i in newNewList:
		out.write(str(i[0] + "\t"))
		tempStr = ""
		while len(i[1]) != 0:
			tempStr += str(i[1].pop()) + "\t"
		out.write(tempStr + "\n")
 
#Because Dr. Lu told me to
tss.close()
common.close()
out.close()