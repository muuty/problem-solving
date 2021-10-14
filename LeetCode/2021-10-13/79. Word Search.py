def dfs(point, history, board, i, word):
	if i == len(word):
		return True
	target = word[i]

	tmp = board[point[0]][point[1]]
	board[point[0]][point[1]] = "#"
	for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		if 0 <= point[0] + dx < len(board) and 0 <= point[1] + dy < len(board[0]):
			if target == board[point[0] + dx][point[1] + dy]:
				if dfs((point[0] + dx, point[1] + dy), history + [(point[0] + dx, point[1] + dy)], board, i + 1, word):
					return True
	board[point[0]][point[1]] = tmp
	return False


class Solution(object):
	def exist(self, board, word):
		starts = [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == word[0]]
		for start in starts:
			if dfs(start, [start], board, 1, word):
				return True

		return False




print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))