def solution(n, s, a, b, fares):

	cost = [[float("inf")] * n for _ in range(n)]

	for i in range(n):
		cost[i][i] = 0

	for fare in fares:
		i,j,value = fare
		cost[i-1][j-1] = value
		cost[j-1][i-1] = value


	for k in range(n):
		for i in range(n):
			for j in range(i+1, n):
				if cost[i][j] > cost[i][k] + cost[k][j]:
					cost[i][j] = cost[i][k] + cost[k][j]
					cost[j][i] = cost[i][j]

	return min([cost[s-1][k] + cost[k][a-1] + cost[k][b-1] for k in range(n)])


print(solution(7,3,4,1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	))
print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))