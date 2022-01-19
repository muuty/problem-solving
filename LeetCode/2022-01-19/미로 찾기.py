import heapq
from collections import defaultdict
INF = float('inf')


def solution(n, start, end, roads, traps):
    answer = INF
    min_cost = [[INF for _ in range(n+1)] for _ in range(2**len(traps))]

    trap_index = {v: i for i, v in enumerate(traps)}
    graph = defaultdict(dict)
    for start, end, cost in roads:
        graph[start][end] = (cost, False)
        graph[end][start] = (cost, True)

    q = []

    heapq.heappush(q, (0, start, 0))  # distance_sum, position, state
    min_cost[0][start] = 0

    while q:
        _sum, _pos, _state = heapq.heappop(q)
        if _pos == end:
            answer = min(answer, _sum)
            continue
        if _sum > min_cost[_state][_pos]:
            continue
        for next_pos in graph[_pos]:
            cost, is_reverse = graph[_pos][next_pos]

            if not can_go(_pos, next_pos, _state, trap_index, is_reverse):
                continue

            next_state = get_next_state(next_pos, _state, trap_index)
            next_sum = cost + _sum
            if next_sum >= min_cost[next_state][next_pos]:
                continue

            min_cost[next_state][next_pos] = next_sum
            heapq.heappush(q, (next_sum, next_pos, next_state))

    return answer


def can_go(from_pos, to_pos, trap_state, trap_index, is_reverse):
    from_trap_on, to_trap_on = False, False
    if from_pos in trap_index:
        from_trap_on = (trap_state & (1 << trap_index[from_pos])) == 1
    if to_pos in trap_index:
        to_trap_on = (trap_state & (1 << trap_index[to_pos])) == 1

    return is_reverse == (from_trap_on != to_trap_on)


def get_next_state(next_pos, cur_state, trap_to_index):
    if next_pos in trap_to_index:
        return cur_state ^ (1 << trap_to_index[next_pos])
    return cur_state

print(solution(3, 1,3,[[1, 2, 2], [3, 2, 3]]	,[2]))