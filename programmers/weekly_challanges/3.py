def dfs(i, j, current_cluster, clusters, visited, X, Y, board, block_or_empty):
    if not (0 <= i < X and 0 <= j < Y and board[i][j] == block_or_empty and (i,j) not in visited):
        return

    dxy = [[0,1], [0,-1], [1,0], [-1,0]]
    visited.add((i, j))
    current_cluster.append((i, j))
    for dx, dy in dxy:
        dfs(i + dx, j + dy, current_cluster, clusters, visited, X, Y, board, block_or_empty)

def arrange_block(block):
    block.sort(key=lambda x: x[1])
    block.sort(key=lambda x: x[0])
    return [[pos[0] - block[0][0], pos[1] - block[0][1]] for pos in block]

def rotate(point):
    return [point[1], -point[0]]

def is_same(block1, block2):
    for i in range(len(block1)):
        if block1[i][0] != block2[i][0] or block1[i][1] != block2[i][1]:
            return False
    return True


def rotate_and_check(block1, block2):
    if len(block1) != len(block2):
        return False
    block1 = arrange_block(block1)
    block2 = arrange_block(block2)
    for i in range(0, 4):
        if is_same(block1, block2):
            return True
        block2 = arrange_block([rotate(point) for point in block2])
    return False

def get_blocks(board, block_or_empty):
    clusters = []
    visited = set()

    X = len(board)
    Y = len(board[0])
    for i in range(X):
        for j in range(Y):
            if (i,j) not in visited and board[i][j] ==block_or_empty:
                new_cluster = []
                dfs(i,j, new_cluster, clusters, visited, X, Y, board, block_or_empty)
                clusters.append(new_cluster)

    return clusters



def solution(game_board, table):
    emptys = get_blocks(game_board, 0)
    blocks = get_blocks(table, 1)


    used_blocks = set()
    total_filled = 0
    for i in range(len(emptys)):
        for j in range(len(blocks)):
            if j not in used_blocks and rotate_and_check(emptys[i], blocks[j]):
                used_blocks.add(j)
                total_filled += len(blocks[j])
                break

    return total_filled




print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]	))