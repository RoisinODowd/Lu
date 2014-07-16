import sys

###
# Improper argument handling
###
if len(sys.argv) != 5:
	sys.stderr.write("The proper usage of this program is 'python reducer.py [MUTATIONS] [EXPRESSIONS] [CNA] [OutputFile]'\n")
	sys.exit()

print "Please make sure that all matrices have genes as rows and tumors as columns, aka untransposed. If you aren't sure, check now."

###
# Opens multiple files via the command line.
# The mutation matrix is the first argument, the expression the second,
# and the CNA the third.
###
mutFile = open(sys.argv[1], "r")
expFile = open(sys.argv[2], "r")
cnaFile = open(sys.argv[3], "r")

###
# The first line of each line is read, stripped, and split by tabs
# so each tumor is its own element in a list.
#
# mutList = ['Tumor1', 'Tumor2', ...]
# expList = ['Tumor1', 'Tumor2', ...]
# cnaList = ['Tumor1', 'Tumor2', ...]
###
mutList = mutFile.readline().strip().split("\t")
expList = expFile.readline().strip().split("\t")
cnaList = cnaFile.readline().strip().split("\t")

###
# Each list is turned into a set to remove duplicates
# and to allow for the usage of set mathematical functions.
#
# mutSet = {'Tumor1', 'Tumor2', ...}
# expSet = {'Tumor1', 'Tumor2', ...}
# cnaSet = {'Tumor1', 'Tumor2', ...}
###
mutSet = set(mutList)
expSet = set(expList)
cnaSet = set(cnaList)

###
# Since we need to find only the common tumors in all three files,
# the set function intersection is used. This returns a set containing
# only the tumors common between all three files.
#
# commonSet = {'Tumor1', 'Tumor2', ...}
###
commonSet = mutSet.intersection(expSet).intersection(cnaSet)

###
# Opens the given argument as the output file and then prints out
# each tumor on a new line. The output is referred to as the 
# CommonTumors file.
###
with open(sys.argv[4], "w") as out:
	while len(commonSet) > 0:
		temp = commonSet.pop()
		if temp == "Sample":
			continue
		else:
			out.write(temp + "\n")
###
# Closing files
###
mutFile.close()
expFile.close()
cnaFile.close()
out.close()
