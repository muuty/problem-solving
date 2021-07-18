

T, N, B, P =list(map(int, input().split()))


def fill_bottom(number, blocks, block_lens):
    for i in range(len(blocks)):
        if block_lens[i] < B-2:
            blocks[i].append(number)
            block_lens[i] += 1
            return i + 1
    return 0


def fill_top(number, blocks, block_lens):
    for i in range(len(blocks)):
        if block_lens[i] == B-1:
            blocks[i].append(number)
            block_lens[i] += 1
            return i+1
    return 0

def fill_second_top(number, blocks, block_lens):
    for i in range(len(blocks)):
        if block_lens[i] == B-2:
            blocks[i].append(number)
            block_lens[i] += 1
            return i+1
    return 0



for t in range(T):
    blocks = [[] for j in range(N)]
    block_lens = [0 for j in range(N)]
    answer = 0
    for i in range(N*B):
        number = int(input())
        if number < 7:
            answer = fill_bottom(number, blocks, block_lens)
            if answer == 0:
                answer = fill_second_top(number, blocks, block_lens)
                if answer == 0:
                    answer = fill_top(number, blocks, block_lens)
        elif number == 8 or number == 7:
            answer = fill_second_top(number, blocks, block_lens)
            if answer == 0:
                answer = fill_bottom(number, blocks, block_lens)
                if answer == 0:
                    answer = fill_top(number, blocks, block_lens)
        elif number == 9:
            answer = fill_top(number, blocks, block_lens)
            if answer == 0:
                answer = fill_second_top(number, blocks, block_lens)
                if answer == 0:
                    answer = fill_bottom(number, blocks, block_lens)
        print(answer)
