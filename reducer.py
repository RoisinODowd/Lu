import sys

"""
Improper argument handling
"""
if len(sys.argv) != 4:
	sys.stderr.write("The proper usage of this program is 'python reducer.py [EXPRESSIONS] [CNA] [OutputFile]'\n")
	sys.exit()

"""
Opens multiple files via the command line.
The mutation matrix is the first argument, the expression the second,
and the CNA the third. The first line in each file is skipped.
"""
expFile = open(sys.argv[1], "r")
cnaFile = open(sys.argv[2], "r")
next(expFile)
next(cnaFile)

"""
The first column of each line, the TCGA id, is appended to the
respective list.

mutList = ['Tumor1', 'Tumor2', ...]
expList = ['Tumor1', 'Tumor2', ...]
cnaList = ['Tumor1', 'Tumor2', ...]
"""
for line in expFile:
	expList.append(line.split("\t")[0])
for line in cnaFile:
	cnaList.append(line.split("\t")[0])
"""
Each list is turned into a set to remove duplicates
and to allow for the usage of set mathematical functions.

mutSet = {'Tumor1', 'Tumor2', ...}
expSet = {'Tumor1', 'Tumor2', ...}
cnaSet = {'Tumor1', 'Tumor2', ...}
"""
expSet = set(expList)
cnaSet = set(cnaList)

"""
Since we need to find only the common tumors in all three files,
the set function intersection is used. This returns a set containing
only the tumors common between all three files.

commonSet = {'Tumor1', 'Tumor2', ...}
"""
commonSet = expSet.intersection(cnaSet)

"""
Opens the given argument as the output file and then prints out
each tumor on a new line. The output is referred to as the 
CommonTumors file.
"""
with open(sys.argv[3], "w") as out:
	while len(commonSet) > 0:
		temp = commonSet.pop()
		if temp == "Sample":
			continue
		else:
			out.write(temp + "\n")
"""
Closing files
"""
expFile.close()
cnaFile.close()
out.close()
