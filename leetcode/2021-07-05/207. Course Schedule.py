import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        n = numCourses
        visited = [0] * n
        graph = collections.defaultdict(set)
        for pre in prerequisites:
            graph[pre[0]].add(pre[1])

        def dfs(i, graph, visited):
            if visited[i] == 1:
                return True
            elif visited[i] == -1:
                return False
            else:
                visited[i] = -1
                for j in graph[i]:
                    if dfs(j, graph, visited) == False:
                        return False
                visited[i] = 1
                return True

        for i in range(0, n):
            if i not in visited:
                if dfs(i, graph, visited) == False:
                    return False

        return True



print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
#print(Solution().canFinish(2, [[1,0], [0,1]]))