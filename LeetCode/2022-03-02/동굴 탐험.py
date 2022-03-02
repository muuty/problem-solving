from collections import defaultdict


def solution(n, path, order):
    before = defaultdict(int)
    after = defaultdict(int)
    nodes = defaultdict(set)

    for i in range(len(path)):
        v1, v2 = path[i][0], path[i][1]
        nodes[v1].add(v2)
        nodes[v2].add(v1)

    for i in range(len(order)):
        if order[i][1] == 0:
            return False
        before[order[i][1]] = order[i][0]

    stack = [0]
    visited = [False] * n

    while stack:
        tmp_node = stack.pop()
        if tmp_node in before and not visited[before[tmp_node]]:
            after[before[tmp_node]] = tmp_node
            continue

        visited[tmp_node] = True
        for adj in nodes[tmp_node]:
            if not visited[adj]:
                stack.append(adj)

        if tmp_node in after:
            stack.append(after[tmp_node])

    return True if False not in visited else False


print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	,[[4,1],[8,7],[6,5]]))
