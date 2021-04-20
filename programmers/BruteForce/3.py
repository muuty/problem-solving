def solution(brown, yellow):
    # brown = 2x + 2y -4
    # yellow = (x-2)*(y-2)

    for y in range(1, (brown + 4) // 2):
        x = (brown + 4 - 2 * y) // 2
        if yellow == (x - 2) * (y - 2):
            return [x, y]


solution(10, 2)