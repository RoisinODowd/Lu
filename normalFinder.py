import sys

if len(sys.argv) != 3:
	sys.stderr.write("The proper usage of this proram is 'python normalFinder.py [EXPRESSION_MATRIX] [OutputFile]'\n")
	sys.exit()

gm = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")
next(gm)

for line in gm:
	twoDigClass = int(line.strip().split("\t")[0][13:])
	if twoDigClass < 20 and twoDigClass >= 10:
		out.write(line)

gm.close()
out.close()