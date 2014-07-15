import sys

"""
Improper argument handling
"""
if len(sys.argv) != 3:
	sys.stderr.write("The proper usage of this program is 'python normalFinder.py [EXPRESSION_MATRIX] [OutputFile]'\n")
	sys.exit()

"""
Open two files: an expression matrix that is tumors x genes, and
an output file.
"""
gm = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

"""
Read the first line of the expression matrix, the genes, into a
variable so it can be written once.
"""
header = gm.readline()

"""
Write header.
"""
out.write(header)

"""
Go through each line in the expression matrix and get the two letter
code for each TCGA id. If the TCGA id is greater or equal to 10 and
less than 20, then it is a normal sample and the entire line is written
to output.
"""
for line in gm:
	twoDigClass = int(line.strip().split("\t")[0].split("-")[3])
	if twoDigClass < 20 and twoDigClass >= 10:
		out.write(line)

"""
Closing files
"""
gm.close()
out.close()
