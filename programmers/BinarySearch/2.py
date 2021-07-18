def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()

    left = 1
    right = distance

    while left <= right:
        mid = (left + right) // 2
        current_location = 0
        remove_count = 0
        min_distance = 987654321
        for rock in rocks:
            diff = rock - current_location
            if diff < mid:
                remove_count += 1
            else:
                current_location = rock
                min_distance = min(min_distance, diff)

        if remove_count > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer