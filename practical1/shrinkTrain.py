# Used to shrink training data for experimentation
with open('data/train.csv') as f:
	with open('data/train1000.csv', 'w') as outfile:
		for i in xrange(1001):
			outfile.write(f.readline())