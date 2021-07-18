import math


def solution(progresses, speeds):
    remain = [math.ceil(float(100 - progresses[i]) / float(speeds[i])) for i in range(len(speeds))]
    print(remain)
    counts = []
    count = 0
    release_day = -1
    for i in range(len(remain)):
        if remain[i] > release_day:
            if i != 0:
                counts.append(count)
            release_day = remain[i]
            count = 1
        else:
            count += 1
    counts.append(count)
    return counts





print(solution([93, 30, 55]	,  	[1, 30, 5]))