from collections import deque


def solution(n, edges):

    graph = {i : [] for i in range(n+1)}

    queue = deque()

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = {i: False if i!= 1 else True for i in range(n+1)}
    queue.append((1, 1))

    max_length_nodes = []
    max_length = 0
    while queue:
        node, length = queue.popleft()
        if length > max_length:
            max_length_nodes = []
            max_length_nodes.append(node)
            max_length = length
        elif length == max_length:
            max_length_nodes.append(node)

        next_nodes = [i for i in graph[node] if not visited[i]]
        for next_node in next_nodes:
            visited[next_node] = True
            queue.append((next_node, length+1))

    return len(max_length_nodes)

if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))