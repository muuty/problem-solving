from collections import defaultdict


def solution(info, edges):
    edges.sort()
    path = defaultdict(list)
    remain_sheeps = set([i for i, value in enumerate(info) if value == 0])
    wolfs = set([i for i, value in enumerate(info) if value == 1])

    for edge in edges:
        path[edge[1]] = path[edge[0]] + [edge[0]]

    visited = {0}
    sheep_count = 1
    wolf_count = 0
    answer = [1]
    remain_sheeps.remove(0)  # already visited

    for sheep in remain_sheeps:
        dfs(sheep, remain_sheeps - {sheep}, path, sheep_count, wolf_count, wolfs, visited, answer)
    return answer[0]


def dfs(current, remain, path, sheep_count, wolf_count, wolfs, visited, answer):
    if get_wolfs_on_path(current, wolfs, path, visited) + wolf_count >= sheep_count:
        # current 로 갈 수 없음. 종료
        return

    sheep_count += 1
    wolf_count += get_wolfs_on_path(current, wolfs, path, visited)

    answer[0] = max([answer[0], sheep_count])

    for sheep in remain:
        dfs(sheep, remain - {sheep}, path, sheep_count, wolf_count, wolfs, visited | set(path[current]), answer)


def get_wolfs_on_path(destination, wolfs, path, visited):
    return sum([1 for i in path[destination] if i in wolfs and i not in visited])


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0]	, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	))
