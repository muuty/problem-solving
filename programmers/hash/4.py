import heapq


def solution(genres, plays):
    _sum = {}
    best = {}
    for i in range(len(genres)):
        if genres[i] not in best:
            best[genres[i]] = []
            _sum[genres[i]] = 0

        _sum[genres[i]] += plays[i]
        heapq.heappush(best[genres[i]], [-1 * plays[i], i])

    top_genres = [[genre, _sum[genre]] for genre in _sum]
    top_genres.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for item in top_genres:
        genre = item[0]
        answer.append(heapq.heappop(best[genre])[1])
        answer.append(heapq.heappop(best[genre])[1])

    return answer



print(solution(["classic", "pop", "classic", "classic", "pop"]	,[500, 600, 150, 800, 2500]	 ))