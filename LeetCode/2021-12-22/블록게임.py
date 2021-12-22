
CAN_REMOVE = 0
CAN_NOT_REMOVE = -1
CHECKED_EVERY_BLOCK = -2


def solution(board):
    n = len(board)
    result = 0

    while True:
        for i in range(n):
            upper_blocks = set([v for v in board[i][:] if v not in [0, -1]])

            if i == n-1 and not upper_blocks:
                return result

            remove_exist = True
            not_removed = []
            while remove_exist:
                remove_exist = False
                upper_blocks = set([v for v in board[i][:] if v not in [0, -1]])
                for block in upper_blocks:
                    if CAN_REMOVE == is_removable(board, block):
                        remove_block(board, block, 0)
                        remove_exist = True
                        result += 1
                    else:
                        not_removed.append(block)
            for block in not_removed:
                remove_block(board, block, CAN_NOT_REMOVE)


def is_removable(board, current_block):

    n = len(board)
    checked_current_block = 1
    found = False
    while checked_current_block < 4:
        for i in range(n):
            for j in range(n):
                if i == n - 1 and j == n - 1:
                    return CAN_NOT_REMOVE

                if found and board[i][j] == current_block:
                    # unable to remove block
                    if not is_upper_empty(board, i, j, current_block):
                        #print(i, j, "3 not ", current_block)
                        return CAN_NOT_REMOVE
                    else:
                        checked_current_block += 1
                        #print(i,j, "checked", checked_current_block)
                        if checked_current_block == 4:
                            #print("can remove")
                            return CAN_REMOVE
                if not found and board[i][j] != 0 and board[i][j] != -1:
                    found = True
                    # print("found block", i, j, "value: ", board[i][j])

                    # filter   X X X , X X X, X X X , X X , X X
                    #           X     X          X , X       X
                    #                                x       X
                    if (j > 0 and board[i][j - 1] == current_block) or (
                            j < len(board) - 1 and board[i][j + 1] == current_block):
                        #print("2 not")
                        return CAN_NOT_REMOVE

                    # filter     X         X
                    #            X X  ,  X X
                    #            X         X
                    if i < n - 3 and board[i + 2][j] == current_block:
                        if (j > 0 and board[i+1][j - 1] == current_block) or (
                                j < len(board) - 1 and board[i+1][j + 1] == current_block):
                            #print("1 not")
                            return CAN_NOT_REMOVE

def remove_block(board, k, value):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == k:
                board[i][j] = value
                count += 1

            if count == 4:
                return


def is_upper_empty(board, i, j, current_block):
    for y in range(0, i):
        if board[y][j] not in [0, current_block]:
            return False
    return True

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))


print(solution(
    [[0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
))

print(solution(
    [[0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,2,0,0],
    [0,3,2,2,2],
    [0,3,3,3,0]]
))
print(solution(
    [[0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,2,0,0],
    [0,3,2,2,2],
    [0,3,3,3,0]]
))
print(solution(
    [[0,1,1,0,0],
    [0,2,1,0,0],
    [0,2,1,0,0],
    [0,2,2,0,0],
    [0,0,0,0,0]]
))


print(solution(
    [[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,2,0,0],
    [0,2,2,2,0]]
))


print(solution(
    [[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,1,1,1,0]]
))

print(solution(
    [[0,0,0,0,0],
    [1,0,0,2,0],
    [1,2,2,2,0],
    [1,1,0,0,0],
    [0,0,0,0,0]]
))