from collections import deque, defaultdict


def can_rotate(p1, p2, new_p1, new_p2, board):
    same = p1 if p1 == new_p1 else p2
    if is_available(new_p1, new_p2, board):
        print(new_p1, new_p2, same)
        required = (new_p1[0] + new_p2[0] + p1[0] + p2[0] - 3*same[0], new_p1[1] + new_p2[1] + p1[1] + p2[1] - 3*same[1])
        print(required)
        if board[required[0]][required[1]] == 0:
            return True
    return False

def is_available(p1, p2, board):
    for x, y in [p1, p2]:
        if not (0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0):
            return False
    return True


def solution(board):
    queue = deque()
    visited = dict()
    queue.append([(0,0),(0,1),0])
    while queue:
        print(queue)
        p1, p2, distance = queue.popleft()
        if p1[0] == len(board)-1 and p1[1] == len(board[0]) -1:
            return distance
        if p2[0] == len(board)-1 and p2[1] == len(board[0]) -1:
            return distance
        # move
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_p1 = (p1[0] + dx, p1[1] + dy)
            new_p2 = (p2[0] + dx, p2[1] + dy)
            if is_available(new_p1, new_p2, board) and not (new_p1[0] + new_p2[0], new_p1[1] + new_p2[1]) in visited:
                visited[(new_p1[0] + new_p2[0], new_p1[1] + new_p2[1])] = distance + 1
                queue.append([new_p1, new_p2, distance + 1])

        # rotate
        if p1[0] == p2[0]:
            new_points = [[p1, (p1[0] + 1, p1[1])], [p1, (p1[0] - 1, p1[1])], [p2, (p2[0] + 1, p2[1])], [p2, (p2[0] - 1, p2[1])]]

            for new_point in new_points:
                if can_rotate(p1, p2, new_point[0], new_point[1], board) and not (new_point[0][0] + new_point[1][0], new_point[0][1] + new_point[1][1]) in visited:
                    visited[(new_point[0][0] + new_point[1][0], new_point[0][1] + new_point[1][1])] = distance + 1
                    queue.append([new_point[0], new_point[1], distance + 1])

        if p1[1] == p2[1]:
            new_points = [[p1, (p1[0], p1[1] + 1)], [p1, (p1[0], p1[1] - 1)], [p2, (p2[0], p2[1] + 1)], [p2, (p2[0], p2[1] - 1)]]
            for new_point in new_points:
                if can_rotate(p1, p2, new_point[0], new_point[1], board) and not (new_point[0][0] + new_point[1][0], new_point[0][1] + new_point[1][1]) in visited:
                    visited[(new_point[0][0] + new_point[1][0], new_point[0][1] + new_point[1][1])] = distance + 1
                    queue.append([new_point[0], new_point[1], distance + 1])



#print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0,0,0],[0,1,0],[0,0,0]]))