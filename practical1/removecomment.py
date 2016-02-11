lines = []

with open("new_features.csv") as infile:
	lines = infile.readlines()

lines[0] = lines[0][2:]

print lines[0]

with open("new_features2.csv", "w") as outfile:
	for i in xrange(len(lines)):
		outfile.write(lines[i])