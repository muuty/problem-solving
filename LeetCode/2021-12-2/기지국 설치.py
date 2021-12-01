def solution(n, stations, w):
    last_covered = 0
    answer = 0

    for station in stations:
        remain = station - w - last_covered - 1
        if remain > 0:
            new_stations = remain // (2*w+1) + (remain % (2*w+1) > 0)
            answer += new_stations
            last_covered = station + w

    remain = n - stations[-1] - w - 1
    if remain > 0:
        new_stations = remain // (2*w + 1) + (remain % (2*w+1) > 0)
        answer += new_stations
    return answer


print(solution(11,[4,11],1))
print(solution(16,[9], 2))
