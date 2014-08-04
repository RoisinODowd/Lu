import sys

expMatrix = open(sys.argv[1], "r")
binCDF = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

tumorIds = []
for line in expMatrix:
	tumorIds.append(line.split("\t")[0])
tumorIds.remove('sample')

expMatrix.seek(0)

out.write(expMatrix.readline())
count = 0
for line in binCDF:
	out.write(tumorIds[count] + "\t" + line)
	count += 1
out.close()