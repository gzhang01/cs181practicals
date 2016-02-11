# Used to remove the comment that results from including header
lines = []

with open("data/new_features_commented.csv") as infile:
	lines = infile.readlines()

lines[0] = lines[0][2:]

print lines[0]

with open("data/new_features.csv", "w") as outfile:
	for i in xrange(len(lines)):
		outfile.write(lines[i])