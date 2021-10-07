class Solution(object):
    def isBipartite(self, graph):
        partition = dict()

        def dfs(pos):
            for neighbor in graph[pos]:
                if neighbor in partition:
                    if partition[neighbor] == partition[pos]:
                        return False
                else:
                    partition[neighbor] = 1 - partition[pos]
                    if not dfs(neighbor):
                        return False
            return True
        for i in range(len(graph)):
            if i not in partition:
                partition[i] = 0
                if not dfs(i):
                    return False
        return True


print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))