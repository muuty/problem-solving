class Solution(object):
    def knightProbability(self, N, K, r, c):
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        mem = {}

        def dfs(k, x, y, P):
            p = 0
            if 0 <= x < N and 0 <= y < N:
                if k < K:
                    for dx, dy in moves:
                        x_next = x + dx
                        y_next = y + dy
                        if (x_next, y_next, k + 1) not in mem:
                            mem[(x_next, y_next, k + 1)] = dfs(k + 1, x_next, y_next, P / 8)
                        p += mem[(x_next, y_next, k + 1)]
                else:
                    p = P

            return p

        return dfs(0, r, c, 1.0)


