def solution(lines):
	points = set()
	lines = [[float(line[0]), float(line[1]), float(line[2])] for line in lines]
	min_x, min_y = float('inf'), float('inf')
	max_x, max_y = float('-inf'), float('-inf')
	for i in range(len(lines)):
		for j in range(i + 1, len(lines)):
			A, B, E = lines[i]
			C, D, F = lines[j]
			if A * D - B * C != 0:
				x = (B * F - E * D) / (A * D - B * C)
				y = (E * C - A * F) / (A * D - B * C)
				if x - int(x) == 0 and y - int(y) == 0:
					x = int(x)
					y = int(y)
					points.add((x, y))
					min_x = min([min_x, x])
					max_x = max([max_x, x])
					min_y = min([min_y, y])
					max_y = max([max_y, y])

	board = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
	print(min_x, max_x, min_y, max_y)
	for line in board:
		print(line)
	for point in points:
		x, y = point
		print(x, y, x - min_x, max_y - y)
		board[max_y - y][x - min_x] = '*'

	board = [''.join(line) for line in board]
	return board


print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]	))
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	))
print(solution([[1,0,0], [0,1,0], [3,4,-12]]))