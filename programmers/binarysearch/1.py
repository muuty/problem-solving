import heapq


def solution(n, times):
    speeds = [1.0 / time for time in times]

    total_speed = sum(speeds)
    required_time = int(n / total_speed)
    passed = [int(required_time * speed) for speed in speeds]
    print(passed)
    lines = []
    for i in len(times):
        heapq.heappush(lines, [(passed + 1) * times[i], times[i]])

    for i in range(n - sum(passed)):
        line = heapq.heappop(lines)
        if i == n - 1:
            return line[0]
        line[0] += line[1]
        heapq.heappush(lines, line)


print(solution(6, [7, 10]))