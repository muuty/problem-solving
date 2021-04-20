import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    for op in operations:
        action, number = op.split()
        number = int(number)
        if action == 'I':
            heapq.heappush(max_heap, -1 * number)
            heapq.heappush(min_heap, number)

        elif action == 'D':
            if len(min_heap) == 0:
                continue

            if number == 1:
                max_number = heapq.heappop(max_heap)
                min_heap.remove(-1 * max_number)
            else:
                min_number = heapq.heappop(min_heap)
                max_heap.remove(-1 * min_number)

    if min_heap:
        answer = [-1 * heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        answer = [0, 0]
    return answer