def solution(food_times, k):
    values = sorted(food_times)
    max_value = max(food_times)
    removed_value = 0
    removed_count = 0
    for i in range(len(values)):
        current_value = values[i] - removed_value
        count = len(values) - i
        if k >= current_value * count:
            removed_count += 1
            removed_value += current_value
            k -= current_value * count
        else:
            break
    if removed_value == max_value:
        return -1
    remains = len(food_times) - removed_count
    k = k % remains
    for i in range(len(food_times)):
        if food_times[i] > removed_value:
            if k == 0:
                return i + 1
            k -= 1



#print(solution([3, 1, 2], 5))
#print(solution([3,3,3], 9))
#print(solution([3,3,4],9))
print(solution([1, 5, 5, 5, 5, 6, 7], 31))