def dijkstra(x1, y1, x2, y2, remain_cards):
    if x1 == x2 or y1 == y2:
        return 1 + 1
    elif x2 in [0,3] or y2 in [0,3]:
        return 2 + 1
    else:
        return abs(x1 - x2) + abs(y1-y2) + 1

def get_move_count(x1, y1, x2, y2, remain_cards):
    if x1 == x2 or y1 == y2:
        return 1 + 1
    elif x2 in [0,3] or y2 in [0,3]:
        return 2 + 1
    else:

        return abs(x1 - x2) + abs(y1-y2) + 1

def dfs(current_card, remain_cards, history, count, min_count):
    x,y,num = current_card
    if len(remain_cards) == 0:
        print(history, count)
        if count < min_count[0]:
            min_count[0] = count
        return
    elif len(remain_cards) %2 == 1:
        next_card = [card for card in remain_cards if card[2] == num][0]
        move_count = get_move_count(x,y, next_card[0], next_card[1])
        dfs(next_card, remain_cards - {next_card}, history + [next_card[2]], count + move_count, min_count)
    else:
        for next_card in remain_cards:
            move_count = get_move_count(x,y, next_card[0], next_card[1])
            dfs(next_card, remain_cards - {next_card}, history + [next_card[2]],count + move_count, min_count)


def solution(board, r, c):
    cards = set((x,y,board[x][y]) for x in range(0,4) for y in range(0,4) if board[x][y] != 0)
    print(cards)
    answer = [float('inf')]
    for card in cards:
        move_count = get_move_count(c,r, card[0], card[1])
        dfs(card, cards - set(card), [], move_count, answer)

    return answer[0]

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))