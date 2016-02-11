with open('train.csv') as f:
	with open('train_small.csv', 'w') as outfile:
		for i in xrange(1001):
			outfile.write(f.readline())

