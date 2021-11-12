from collections import defaultdict
import bisect

import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, num, x, y, left=None, right=None):
        self.num = num
        self.parent = None
        self.x = x
        self.y = y
        self.left = left
        self.right = right
        self.right_range = float('inf')

    def __lt__(self, other):
        return self.x < other.x


def preorder(root, result):
    if root:
        result.append(root.num)
        preorder(root.left, result)
        preorder(root.right, result)


def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.num)


def generate_tree(nodeinfo):
    nodes = defaultdict(list)  # dict(level) = [nodes]
    levels = list()
    root = None
    for i, node in enumerate(nodeinfo):
        x, y = node
        node = Node(i+1, x, y)
        if y not in nodes:
            bisect.insort(levels, y)
        bisect.insort(nodes[y], node)
    prev_level = None

    levels.reverse()

    for level in levels:
        if not prev_level:  # top node
            prev_level = level
            root = nodes[level][0]
            continue

        current_nodes = nodes[level]
        upper_nodes = nodes[prev_level]
        j = 0
        for i in range(0, len(current_nodes)):
            if upper_nodes[j].parent:
                while upper_nodes[j].right_range < current_nodes[i].x:
                    j += 1

            if current_nodes[i].x < upper_nodes[j].x:
                # connect
                upper_nodes[j].left = current_nodes[i]
                current_nodes[i].parent = upper_nodes[j]

                # set range
                current_nodes[i].right_range = upper_nodes[j].x

            elif current_nodes[i].x > upper_nodes[j].x:
                # connect
                upper_nodes[j].right = current_nodes[i]
                current_nodes[i].parent = upper_nodes[j]

                # set range
                current_nodes[i].right_range = upper_nodes[j].right_range

        prev_level = level
    return root


def solution(nodeinfo):
    root = generate_tree(nodeinfo)
    result_preorder = []
    preorder(root, result_preorder)
    result_postorder = []
    postorder(root, result_postorder)

    return [result_preorder, result_postorder]


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))