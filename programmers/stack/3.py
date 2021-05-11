from collections import deque



def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    time_queue = deque()
    current_time = 0
    current_weight_sum = 0
    while truck_queue:
        current_time += 1

        if time_queue and current_time == time_queue[0][0]:
            time, truck_weight = time_queue.popleft()
            current_weight_sum -= truck_weight
        if weight - current_weight_sum >= truck_queue[0]:
            truck_weight = truck_queue.popleft()
            current_weight_sum += truck_weight
            time_queue.append([current_time + bridge_length, truck_weight])

    if time_queue:
        current_time = time_queue[-1][0]

    return current_time


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, 	[10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))