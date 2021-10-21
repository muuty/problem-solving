class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def get_dp(i,j, dp, matrix):
            if (i,j) in dp:
                return dp[(i,j)]

            next_candidates = []
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<= i+x < len(matrix) and 0 <= j+y < len(matrix[0]):
                    if matrix[i][j] < matrix[i+x][j+y]:
                        next_candidates.append([i+x, j+y])
            if not next_candidates:
                dp[(i,j)] = 1
            else:
                dp[(i,j)] = max(get_dp(next_i, next_j, dp, matrix) for next_i, next_j in next_candidates) + 1

            return dp[(i,j)]

        longest_path_len = 0
        dp = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                path_len = get_dp(i, j, dp, matrix)
                if longest_path_len < path_len:
                    longest_path_len = path_len
        return longest_path_len

print(Solution)