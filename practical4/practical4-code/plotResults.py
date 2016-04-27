import matplotlib.pyplot as plt

# Data to plot
arr = [
		[0, 0, 0, 0, 0, 2, 2, 1, 1, 4, 2, 1, 1, 2, 1, 1, 1, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 1, 2, 0, 1, 2, 0, 2, 1, 3, 1, 1, 13, 0, 1, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 3, 1, 1, 0, 0, 0, 0, 4, 0, 11, 100, 2, 1, 0, 8, 0, 0, 0, 0, 0, 11, 2, 0, 1, 0, 0, 0, 2, 0, 5, 3, 0, 0, 0, 4, 2, 1, 0, 1, 0, 0, 0, 0, 0, 2], 				# 4. No gravity
		[0, 0, 0, 1, 1, 0, 1, 7, 0, 2, 0, 0, 5, 0, 1, 0, 0, 2, 2, 1, 1, 0, 4, 6, 2, 2, 1, 2, 6, 0, 1, 0, 1, 4, 0, 0, 0, 1, 0, 2, 0, 3, 1, 0, 3, 3, 15, 2, 1, 0, 20, 2, 4, 0, 8, 2, 10, 2, 1, 1, 0, 0, 1, 0, 0, 0, 0, 4, 1, 8, 1, 2, 0, 1, 4, 0, 24, 0, 0, 0, 56, 0, 3, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 3, 0, 0],				# 5. Added gravity
		[0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 1, 2, 0, 2, 3, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 3, 0, 2, 0, 0, 1, 2, 1],					# 7. Added velocity
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 2, 0, 4, 1, 1, 2, 0, 0, 3, 1, 0, 3, 4, 2, 0, 5, 1, 1, 0, 1, 4, 0, 3, 9, 15, 1, 0, 1, 17, 2, 18, 1, 2, 4, 9, 3, 1, 2, 0, 6, 1, 4, 0, 6, 28, 0, 45, 1, 13, 0, 0, 2, 41, 3, 7, 0, 0, 0, 34, 1, 0, 9, 47, 0, 0, 15, 0, 1, 0, 0, 0, 1, 1, 0, 3, 0, 0, 0, 2, 1, 0, 0, 0, 2, 0, 0],			# 8. Starting gravity = -4
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 2, 3, 1, 3, 4, 1, 0, 2, 3, 0, 1, 3, 6, 10, 3, 3, 7, 1, 11, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 7, 2, 0, 1, 0, 0, 6, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],					# 9. gamma = 0.2
		[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 2, 1, 2, 0, 0, 1, 1, 1, 2, 2, 0, 2, 1, 2, 0, 1, 2, 3, 4, 1, 0, 8, 4, 1, 1, 3, 3, 6, 23, 25, 2, 7, 16, 1, 0, 4, 0, 0, 12, 27, 1, 0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 6, 7, 6, 0, 13, 3, 1, 0, 6, 25, 11, 7, 0, 1, 0, 0, 1, 0, 0, 1, 3, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0],			# 10. gamma = 0.9
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 1, 2, 1, 0, 1, 1, 3, 5, 1, 0, 5, 1, 1, 0, 0, 1, 3, 1, 0, 0, 2, 1, 2, 5, 2, 2, 0, 1, 3, 6, 0, 1, 3, 0, 0, 6, 0, 4, 26, 27, 0, 15, 0, 0, 17, 0, 38, 2, 4, 7, 22, 0, 3, 7, 10, 0, 0, 2, 0, 1, 4, 1, 0, 2, 6, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],			# 11. gamma = 0.5, alpha = 0.8
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 5, 1, 2, 0, 1, 1, 3, 0, 0, 2, 0, 0, 2, 1, 0, 2, 1, 1, 1, 1, 9, 2, 1, 9, 2, 7, 10, 1, 0, 3, 6, 1, 7, 40, 1, 3, 0, 0, 16, 1, 3, 2, 1, 0, 1, 2, 0, 1, 0, 2, 1, 0, 1, 0, 1, 1, 0, 0, 0, 4, 0, 1, 0, 1, 1, 14, 0, 0, 4, 0, 0, 0, 1, 0, 2, 1, 0, 2, 0, 0, 0, 14, 0, 1, 0, 0], 				# 13. updating alpha over time
		[0, 0, 2, 0, 0, 1, 0, 0, 2, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 1, 0, 0, 4, 2, 4, 4, 10, 5, 8, 5, 0, 0, 13, 0, 10, 14, 0, 25, 0, 7, 6, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 5, 7, 2, 2, 0, 0], 				# 14. same conditions as 8
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 0, 0, 2, 2, 3, 5, 2, 2, 1, 0, 2, 1, 10, 0, 2, 0, 1, 2, 6, 3, 2, 1, 7, 1, 1, 1, 1, 5, 3, 3, 1, 7, 1, 3, 2, 2, 10, 0, 0, 5, 7, 0, 0, 2, 45, 15, 3, 0, 16, 0, 6, 0, 70, 0, 2, 1, 53, 0, 3, 0, 219, 2, 0, 69, 0, 249, 1, 358, 247, 18],	# 15. marginBox = 20 
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 1, 1, 2, 0, 3, 1, 1, 0, 5, 1, 0, 3, 5, 1, 1, 3, 3, 1, 1, 6, 3, 8, 1, 1, 2, 10, 5, 2, 7, 11, 6, 1, 2, 3, 6, 1, 1, 2, 12, 4, 20, 2, 2, 0, 5, 5, 55, 18, 11, 2, 1, 114, 3, 0, 102, 1, 29, 1, 0, 0, 2, 44, 5, 32, 2, 43, 0, 0, 1, 2, 10, 1, 9, 6, 8, 16, 4, 1, 1, 5],	# 16. repeat of 15
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 1, 4, 6, 4, 3, 1, 2, 1, 0, 2, 2, 2, 4, 11, 6, 39, 1, 17, 1, 0, 2, 0, 7, 2, 3, 57, 25, 4, 0, 147, 28, 37, 0, 64, 0, 0, 0, 56, 15, 2, 0, 2, 17, 1, 0, 8, 9, 0, 0, 1, 0, 3, 2, 0, 0, 0, 1, 0, 0, 0, 7, 7, 1, 4, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1], 		# 17. marginBox = 30
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 0, 0, 0, 1, 1, 2, 2, 3, 0, 0, 0, 0, 0, 1, 0, 5, 0, 0, 2, 1, 4, 1, 6, 2, 3, 0, 9, 11, 6, 0, 0, 1, 2, 3, 5, 9, 19, 35, 1, 42, 0, 7, 1, 1, 0, 2, 19, 80, 0, 16, 121, 0, 177, 154, 76, 0, 69, 6, 20, 25, 1, 98, 1, 28, 2, 5, 1, 0, 4, 14, 19, 74, 0, 1, 3, 0, 10, 42, 0, 7, 0, 0], # 18. marginBox = 25
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 1, 1, 1, 2, 0, 0, 2, 1, 1, 1, 1, 0, 0, 1, 3, 0, 2, 2, 1, 0, 1, 2, 0, 2, 1, 1, 0, 4, 4, 0, 3, 2, 7, 2, 0, 1, 2, 6, 2, 1, 3, 1, 1, 1, 1, 7, 2, 3, 2, 2, 2, 0, 2, 1, 0, 0, 2, 5, 4, 0, 14, 2, 4, 1, 2, 14, 8, 1, 1, 167, 10, 3, 0, 8, 23, 1, 3, 119, 24, 73, 2, 506, 4, 113],		# 19. Fixed gravity bug
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 2, 0, 1, 2, 2, 0, 1, 1, 2, 2, 0, 2, 9, 4, 1, 0, 1, 1, 5, 5, 38, 3, 21, 1, 3, 1, 10, 20, 8, 3, 1, 164, 3, 432, 2, 76, 1017, 622, 1047, 76, 576, 4, 39, 1, 151, 125, 69, 34, 3, 13, 3, 13, 0, 11, 5, 3, 1, 4, 3, 2, 12, 21, 6, 3, 3, 27, 9, 7, 10, 84, 0, 0, 16, 2, 1, 2, 2, 0, 2], # 20. self.box = 100
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 0, 2, 6, 1, 1, 1, 0, 0, 6, 1, 0, 3, 0, 1, 1, 1, 1, 2, 1, 3, 2, 3, 1, 2, 8, 3, 1, 0, 15, 2, 49, 33, 1, 2, 31, 1, 7, 0, 0, 2, 9, 93, 124, 50, 0, 223, 6, 3, 1, 10, 215, 4, 98, 12, 2, 108, 1, 112, 1, 1, 1, 19, 1, 4, 20, 1, 0, 0, 1, 2, 1, 1, 4, 0, 1, 3, 13, 2, 5, 1, 3, 0, 1, 1], # 21. Repeat of 20
		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 0, 1, 1, 1, 2, 1, 0, 1, 1, 2, 1, 0, 1, 1, 2, 4, 4, 2, 0, 2, 0, 2, 0, 2, 2, 0, 9, 0, 1, 6, 9, 1, 0, 19, 1, 3, 8, 6, 0, 20, 38, 4, 0, 0, 0, 8, 0, 3, 2, 52, 0, 1, 27, 1, 66, 7, 20, 1, 0, 0, 1, 3, 1, 2, 9, 0, 1, 5, 3, 14, 12, 1, 0, 5, 4, 1, 0, 3],			# 22. Added epsilon-greedy (e = 1/tick)
		[0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 2, 8, 0, 2, 4, 2, 1, 3, 2, 3, 8, 1, 1, 1, 1, 1, 2, 1, 3, 2, 1, 12, 1, 19, 5, 1, 1, 14, 2, 4, 3, 1, 3, 36, 6, 1, 1, 12, 2, 2, 3, 11, 1, 1, 3, 1, 0, 39, 4, 89, 15, 17, 2, 28, 1, 1, 0, 3, 2, 10, 1, 3, 2, 0, 1, 1, 2, 21, 0, 2, 0, 2, 11, 0, 3, 5, 3, 5, 1], 	# 23. Epsilon cutoff at 0.01
	]

# Eliminate outliers
for i in xrange(len(arr)):
	c = 0.9
	m = 4
	s = sorted(arr[i])
	print s
	# print s[(int) (len(arr[i]) * c)]
	# print s[(int) (len(arr[i]) * (1 - c))]
	iqr = s[(int) (len(arr[i]) * c)] - s[(int) (len(arr[i]) * (1 - c))]
	upper = s[(int) (len(arr[i]) * c)] + m * iqr
	lower = s[(int) (len(arr[i]) * (1 - c))] - m * iqr
	print upper, lower
	for j in xrange(len(arr[i]) - 1, -1, -1):
		if arr[i][j] > upper or arr[i][j] < lower:
			arr[i].pop(j)

# Format data
x = []
for i in xrange(len(arr)):
	for j in xrange(len(arr[i])):
		x.append(i + 1)
y = [item for sublist in arr for item in sublist]

# Average of data
avgx = [i + 1 for i in xrange(len(arr))]
avgy = [sum(arr[i]) / len(arr[i]) for i in xrange(len(arr))]

# Plot
plt.scatter(x, y, alpha=0.3)
plt.scatter(avgx, avgy, color="red")
plt.savefig("results.png")
plt.show()