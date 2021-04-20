import heapq


def solution(scoville, K):
    count = 0
    heap = scoville
    heapq.heapify(heap)
    while True:
        item = heapq.heappop(heap)
        if item >= K:
            break
        if len(heap) >= 1:
            item2 = heapq.heappop(heap)
            heapq.heappush(heap, item + item2 * 2)
            count += 1
        else:
            return -1

    return count