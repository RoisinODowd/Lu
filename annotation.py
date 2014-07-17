import sys

"""
Improper argument handling
"""
if len(sys.argv) != 2:
	sys.stderr.write("The proper usage of this program is 'python annotation.py [CommonTumorsFile]'\n")
	sys.exit()

"""
Declarations
"""
tss = open("./providedFiles/tissueSourceSite.txt", "r")
common = open(sys.argv[1], "r")

tlcSet = set()
tcgaSet = set()
tumDict = {}
checkList, newList, mergedList = [], [], []

"""
Go through tissueSourceSite.txt and put all the two letter codes 
for cancer types and location into mergedList. These two letter
codes are the second cluster in the TCGA ids in the expression,
mutation, and CNA files. 

mergedList = [['Two letter code', 'Cancer name', set()]]
"""
for codes in tss:
	twoLetCode = {codes.split("\t")[0]}
	tlcSet.update(twoLetCode)
	mergedList.append([codes.split("\t")[0], codes.split("\t")[2], set()])

"""
Since many two letter codes can represent the same type of cancer,
and we only need to print out samples by cancer type, we need to
merge the different cancer names into one id. This is done via the
set declared at mergedList[2]. newList contains tuples with the first
element in the tuple being the cancer name and the second element being
a set.

newList = [('Cancer Name', set())]
"""
for i in range(0, len(mergedList)):
	for j in range(i + 1, len(mergedList)):
		if mergedList[i][1] == mergedList[j][1]:
			temp =  (mergedList[i][1], mergedList[i][2].union(mergedList[j][2])) #local scope declaration
			newList.append(temp)

"""
Sanity check.
I actually have no idea what this is for or why we did this, but
it works.

checkList = [('Cancer name', set())]
"""
for i in newList:
	if i not in checkList:
		checkList.append(i)

"""
Go through the commonTumors file and add each line, which is a TCGA
id, to a set.

tcgaId = 'TCGA-ID-NUMB-XX'
tcgaSet = {'ID1', 'ID2', ...}
"""
for row in common:
	tcgaId = {row.strip()}
	tcgaSet.update(tcgaId)

"""
Goes through each mergedList[i], the two letter code, and compares
it to each two letter code in tcgaSet. If the cancer name in both
mergedList and checkList are the same, then the set in checkList is
updated with the proper TCGA id for that cancer.

temp = 'TCGA-ID-NUMB-XX'
tup = ('Cancer name', set())
"""
while len(tcgaSet) != 0:
	temp = tcgaSet.pop() #local scope declaration
	for i in range(0, len(mergedList)):
		if mergedList[i][0] == temp.split("-")[1]:
			for tup in checkList: #local scope declaration
				if mergedList[i][1] == tup[0]:
					tup[1].update({temp})

"""
Opens an output file called tumorsAnnotated.txt. It first writes
out the cancer name, and then each TCGA id under that cancer delimited
by tabs. Each cancer and its corresponding ids are on one line.
"""
with open("tumorsAnnotated.txt", "w") as out:
	for i in checkList:
		out.write(str(i[0] + "\t"))
		tempStr = ""
		while len(i[1]) != 0:
			tempStr += str(i[1].pop()) + "\t"
		out.write(tempStr + "\n")

"""
Closing files
"""
tss.close()
common.close()
out.close()
