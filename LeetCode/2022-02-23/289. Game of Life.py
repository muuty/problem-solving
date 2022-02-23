class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        original = self.get_board_copy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.get_next_state_cell(i, j, original)


    def get_next_state_cell(self, x, y, board):
        live_neighbors_num = self.get_live_neighbors_num(x, y, board)
        if board[x][y] == 1:
            if live_neighbors_num < 2:
                return 0
            elif live_neighbors_num in (2,3):
                return 1
            else:
                return 0

        else:   # dead cell
            if live_neighbors_num == 3:
                return 1
            else:
                return 0

    def get_board_copy(self, board):
        return [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

    def get_live_neighbors_num(self, x, y, board):
        dxs = (-1, 0, 1)
        dys = (-1, 0, 1)

        live_neighbors_num = 0
        for dx in dxs:
            for dy in dys:
                if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                    live_neighbors_num += board[x + dx][y + dy]

        live_neighbors_num -= board[x][y]
        return live_neighbors_num


print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
