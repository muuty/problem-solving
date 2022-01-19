from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        not_visited = set()
        queue = []
        for j in range(n):
            for i in range(n):
                if grid[j][i] == 1:
                    land = j * n + i
                    queue.append(land)
                else:
                    not_visited.add(land)
        if len(queue) == 0 or len(queue) == n ** 2:
            return -1
        count = 0

        while not_visited:
            new_queue = []
            for candi in queue:
                for d in [n, -n, +1, -1]:
                    new_candi = candi + d
                    if new_candi in not_visited:
                        new_queue.append(new_candi)
                        not_visited.discard(new_candi)
            queue = new_queue
            count += 1
        return count