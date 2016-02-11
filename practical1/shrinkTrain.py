with open('train.csv') as f:
	with open('train1000.csv', 'w') as outfile:
		for i in xrange(1001):
			outfile.write(f.readline())