import sys

in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[2], "w")
first_line = in_file.readline().strip().split("\t")

my_matrix = list()

for i in range(len(first_line)):
	my_matrix.append(list())

in_file.seek(0)

for line in in_file:
	data = line.strip().split("\t")
	for i in range(len(data)):
		my_matrix[i].append(data[i])

for line in my_matrix:
	for data in line:
		out_file.write(data + "\t")
	out_file.write("\n")

