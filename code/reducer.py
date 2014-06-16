import sys
cbio = open(sys.argv[1])
pangea = open(sys.argv[2])

with open("reducerOut.txt", "w") as out:
	for line in pangea:
		for line2 in cbio:
			if line.strip() == line2.strip().split("\t")[0]:
				print line.split("\t")[0]
				out.write(line2)
