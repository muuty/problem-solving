def solution(n, lost, reserve):
    count_list = [1] * n
    for i in lost:
        count_list[i - 1] -= 1

    for i in reserve:
        count_list[i - 1] += 1

    for i in range(0, n):
        if i > 0 and count_list[i] == 0:
            if count_list[i - 1] == 2:
                count_list[i] = 1
                count_list[i - 1] = 1

        if i < n - 1 and count_list[i] == 0:
            if count_list[i + 1] == 2:
                count_list[i] = 1
                count_list[i + 1] = 1

    return sum([1 if value >= 1 else 0 for value in count_list])