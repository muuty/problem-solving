import sys
from collections import deque

readline = sys.stdin.readline

debug_mode = False


def debug_print(*agrs):
    if debug_mode:
        print(agrs)


def submit_question(v1, v2, v3):
    print(v1, v2, v3)

def get_answer():
    return int(input())


class Node:
    def __init__(self, parent, value1= 0, value2 = 0):
        self.values = [value1, value2]
        self.parent = parent
        self.left = None
        self.middle = None
        self.right = None
        self.count = 1


class BTree:
    def __init__(self, head):
        self.head = head
        self.answer = []

    def insert(self, value):
        node = self.head

        while node != None:
            if node.count == 2:
                submit_question(*node.values, value)
                median = get_answer()
                if median == value:
                    if node.middle != None:
                        node = node.middle
                    else:
                        debug_print("middle node :" , value)
                        node.middle = Node(node, value)
                        return
                elif median == node.values[0]:
                    debug_print("left")
                    if node.left != None:
                        node = node.left
                    else:
                        debug_print("left node :" , value)
                        node.left = Node(node, value)
                        return
                elif median == node.values[1]:
                    debug_print("right")
                    if node.right != None:
                        node = node.right
                    else:
                        debug_print("right node :" , value)
                        node.right = Node(node, value)
                        return

            elif node.count == 1:
                if node == node.parent.left or node == node.parent.middle:
                    submit_question(node.values[0], node.parent.values[1], value)
                    median = get_answer()
                    if median == node.values[0]:
                        node.values[1] = node.values[0]
                        node.values[0] = value
                        debug_print("append : ", node.values)
                        node.count += 1
                        return
                    elif median == value:
                        node.values[1] = value
                        debug_print("append : ", node.values)
                        node.count += 1
                        return
                else:
                    submit_question(node.values[0], node.parent.values[0], value)
                    median = get_answer()
                    if median == node.values[0]:
                        node.values[1] = value
                        debug_print("append : ", node.values)

                        node.count += 1
                        return
                    elif median == value:
                        node.values[1] = node.values[0]
                        node.values[0] = value
                        debug_print("append : ", node.values)
                        node.count += 1
                        return

    def print(self):
        self.inorder(self.head)
        print(*self.answer)
        self.answer = []

    def inorder(self, node):
        if node ==None:
            return

        if node.count == 2:
            debug_print("count 2 : ", node.values)
            self.inorder(node.left)
            self.answer.append(node.values[0])
            self.inorder(node.middle)
            self.answer.append(node.values[1])
            self.inorder(node.right)

        elif node.count == 1:
            debug_print("count 1 : ", node.values)
            self.inorder(node.left)
            self.answer.append(node.values[0])
            self.inorder(node.right)

T, N, Q = list(map(int, readline().split()))


for t in range(T):
    submit_question(1,2,3)
    median = get_answer()
    non_median = [i for i in [1,2,3] if i != median]
    head_node = Node(None, *non_median)
    head_node.count = 2
    middle_node = Node(head_node, median)
    btree = BTree(head_node)
    head_node.middle = middle_node

    for i in range(4,N+1):
        btree.insert(i)

    btree.print()
    answer = get_answer()

