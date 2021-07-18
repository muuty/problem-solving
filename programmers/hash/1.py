def solution(participant, completion):
    count = {}
    for name in participant:
        if name not in count:
            count[name] = 0
        count[name] += 1

    for name in completion:
        count[name] -= 1

    answer = [name for name in list(count.keys()) if count[name] > 0]
    return answer[0]