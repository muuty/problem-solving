import sys
input = sys.stdin.readline

T, N, B, P =list(map(int, input().split()))


def fill_bottom(number, blocks, sizes):
    for i in range(len(sizes)):
        if (sizes[i]) < N-1:
            blocks[i].append(number)
            return i + 1
    return 0


def fill_top(number, blocks, sizes):
    for i in range(len(sizes)):
        if (sizes[i]) == N-1:
            blocks[i].append(number)
            return i+1
    return 0

for t in range(T):
    blocks = [[] for j in range(N)]
    sizes = [0 for j in range(N)]
    answer = 0
    for i in range(N*B):
        number = int(input())
        if number < 6:
            answer = fill_bottom(number, blocks, sizes)
            if not answer:
                answer = fill_top(number, blocks, sizes)
        else:
            answer = fill_top(number, blocks, sizes)
            if not answer:
                answer = fill_bottom(number, blocks, sizes)
        print(answer)