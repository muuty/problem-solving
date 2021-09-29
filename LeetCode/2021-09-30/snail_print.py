
'''
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

'''



def print_unit(matrix, unit, x,y, value):
	#if len(unit) == 1:
#		matrix[y][x] = value[0]
#		value[0] += 1
	for i in range(len(unit)):
		for j in range(len(unit)):
			matrix[j+y][i+x] = value[0] + unit[j][i]

	value[0] += len(unit) * len(unit)

def get_snail(size, unit):
	unit_size = len(unit)
	full_size = size
	matrix = [[0] * size * unit_size for _ in range(size*unit_size)]
	current_value = [0]
	while size > 0:
		edge = size - 1
		padding = (full_size - size) // 2
		# right
		for i in range(edge):
			print_unit(matrix, unit, unit_size * (i + padding), unit_size * padding, current_value)

		# down
		for i in range(edge):
			print_unit(matrix, unit, unit_size * (edge + padding), unit_size * (i + padding), current_value)

		# left
		for i in range(edge):
			print_unit(matrix, unit, unit_size * (padding + edge - i), unit_size * (edge + padding), current_value)

		# up
		for i in range(edge):
			print_unit(matrix, unit, unit_size * padding, unit_size * (padding + edge - i), current_value)

		size -= 2
		if size == -1:
			print_unit(matrix, unit, (full_size // 2)*unit_size, (full_size // 2)*unit_size, current_value)


	return matrix



def solution(sizes):
	snail = [[1]]
	for size in sizes:
		snail = get_snail(size, snail)
	print(snail)

solution([2,2])