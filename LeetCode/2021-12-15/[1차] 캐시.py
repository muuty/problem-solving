from collections import deque


def solution(cacheSize, cities):
    cache = set()
    cache_history = deque()

    total_time = 0
    for i in range(len(cities)):
        city = cities[i].upper()
        if city in cache:
            total_time += 1
        else:
            total_time += 5
        cache_history.append(city)

        while len(set(cache_history)) > cacheSize:
            cache_history.popleft()
        cache = set(cache_history)

    return total_time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	))
print(solution(3, [ "SEOUL", "SEOUL", "SEOUL" ]))