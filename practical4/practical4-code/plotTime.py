import matplotlib.pyplot as plt

# Data to plot
arr = [
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 0, 1, 1, 1, 2, 1, 0, 1, 1, 2, 1, 0, 1, 1, 2, 4, 4, 2, 0, 2, 0, 2, 0, 2, 2, 0, 9, 0, 1, 6, 9, 1, 0, 19, 1, 3, 8, 6, 0, 20, 38, 4, 0, 0, 0, 8, 0, 3, 2, 52, 0, 1, 27, 1, 66, 7, 20, 1, 0, 0, 1, 3, 1, 2, 9, 0, 1, 5, 3, 14, 12, 1, 0, 5, 4, 1, 0, 3],			# 22. Added epsilon-greedy (e = 1/tick)
		[0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 2, 8, 0, 2, 4, 2, 1, 3, 2, 3, 8, 1, 1, 1, 1, 1, 2, 1, 3, 2, 1, 12, 1, 19, 5, 1, 1, 14, 2, 4, 3, 1, 3, 36, 6, 1, 1, 12, 2, 2, 3, 11, 1, 1, 3, 1, 0, 39, 4, 89, 15, 17, 2, 28, 1, 1, 0, 3, 2, 10, 1, 3, 2, 0, 1, 1, 2, 21, 0, 2, 0, 2, 11, 0, 3, 5, 3, 5, 1], 	# 23. Epsilon cutoff at 0.01
	]

# Eliminate outliers
# for i in xrange(len(arr)):
# 	c = 0.9
# 	m = 4
# 	s = sorted(arr[i])
# 	print s
# 	# print s[(int) (len(arr[i]) * c)]
# 	# print s[(int) (len(arr[i]) * (1 - c))]
# 	iqr = s[(int) (len(arr[i]) * c)] - s[(int) (len(arr[i]) * (1 - c))]
# 	upper = s[(int) (len(arr[i]) * c)] + m * iqr
# 	lower = s[(int) (len(arr[i]) * (1 - c))] - m * iqr
# 	print upper, lower
# 	for j in xrange(len(arr[i]) - 1, -1, -1):
# 		if arr[i][j] > upper or arr[i][j] < lower:
# 			arr[i][j] = 0


# Format data
for i in xrange(len(arr)):
	x = [j + 1 for j in xrange(len(arr[i]))]
	plt.plot(x, arr[i])
plt.show()

for i in xrange(len(arr)):
	x = [j + 1 for j in xrange(len(arr[i]))]
	plt.plot(x[:20], sorted(arr[i])[::-1][:20])
plt.show()