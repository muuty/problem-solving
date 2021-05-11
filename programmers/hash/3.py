def solution(clothes):
    counts = {}

    for item in clothes:
        if item[1] not in counts:
            counts[item[1]] = 1
        counts[item[1]] += 1

    mul = 1
    for key in counts:
        mul *= counts[key]

    return mul - 1