from collections import defaultdict


class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.presum = defaultdict(int)
        self._init_dp()

    def _init_dp(self):
        self.presum[(0, 0)] = self.matrix[0][0]

        for i in range(1, len(self.matrix)):
            self.presum[(i, 0)] = self.matrix[i][0] + self.presum[(i - 1, 0)]
        for i in range(1, len(self.matrix[0])):
            self.presum[(0, i)] = self.matrix[0][i] + self.presum[(0, i - 1)]

        for n in range(1, len(self.matrix) + len(self.matrix[0])+1):
            for i in range(1, n):
                j = n - i
                if i < len(self.matrix) and j < len(self.matrix[0]):
                    self.presum[(i, j)] = self.matrix[i][j] + self.presum[(i, j - 1)] + self.presum[(i - 1, j)] - self.presum[(i - 1, j - 1)]


    def sumRegion(self, row1, col1, row2, col2):
        return self.presum[(row2, col2)] + self.presum[(row1 - 1, col1 - 1)] - self.presum[(row1 - 1, col2)] - self.presum[(row2, col1 - 1)]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

obj = NumMatrix([[3, 0, 1, 4, 2],
                 [5, 6, 3, 2, 1],
                 [1, 2, 0, 1, 5],
                 [4, 1, 0, 1, 7],
                 [1, 0, 3, 0, 5]])
print(obj.presum)
print(obj.sumRegion(2, 1, 4, 3))
