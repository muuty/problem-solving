from collections import deque

def solution(priorities, location):
    pri_queue = deque(priorities)
    loca_queue = deque([i for i in range(len(priorities))])
    count = 0
    max_priority = max(pri_queue)
    while True:
        _location = loca_queue.popleft()
        priority = pri_queue.popleft()
        if priority < max_priority:
            loca_queue.append(_location)
            pri_queue.append(priority)

        else:
            count += 1
            if _location == location:
                answer = count
                break

            max_priority = max(pri_queue)

    return answer


print(solution([1, 1, 9, 1, 1, 1]	, 0,))