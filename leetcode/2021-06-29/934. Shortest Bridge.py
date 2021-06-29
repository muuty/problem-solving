class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w, h = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(x, y, visited, label, labels):
            if x < 0 or x >= w or y < 0 or y >= h or (x, y) in visited:
                return
            if grid[x][y] == 0:
                labels[(x,y)] = -1
                return

            visited[(x, y)] = True

            if grid[x][y] == 1:
                labels[(x, y)] = label

            for dir in directions:
                dfs(x + dir[0], y + dir[1], visited, label, labels)

        visited = {}
        label = 1
        labels = {}
        for i in range(w):
            for j in range(h):
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j, visited, label, labels)
                    label += 1

        print(labels)


        visited = set()
        minimum_cost = 0
        stack = [(0,0,0, labels[(0,0)])]

        connected_labels = set()


        while stack:
            x,y,cost, label = stack.pop()
            if x>=w or y>=h:
                continue

            if (x,y) not in visited:
                if grid[x][y] == 1:
                    if labels[(x,y)] != label and (labels[(x,y)] not in connected_labels or label not in connected_labels):
                        print(x,y, "connected")
                        minimum_cost += cost
                        connected_labels.add(labels[(x,y)])
                        connected_labels.add(label)
                        visited.add((x,y))
                        stack.append((x+1, y,0, labels[(x,y)]))
                        stack.append((x, y + 1, 0, labels[(x,y)]))
                    else:
                        stack.append((x+1, y,0, label))
                        stack.append((x, y + 1, 0, label))

                elif grid[x][y] == 0:
                    visited.add((x,y))
                    if label != -1:
                        cost = cost+1
                    stack.append((x + 1, y, cost, label))
                    stack.append((x, y+1, cost, label))
        return minimum_cost

print(Solution().shortestBridge([[0,1],[1,0]]))

print(Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))