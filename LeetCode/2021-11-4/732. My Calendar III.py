class MyCalendarThree(object):
    def __init__(self):
        self.tree = BST()

    def book(self, start, end):
        self.tree.root = self.tree.book(start, end, self.tree.root, 1)
        return self.tree.k


class BST:
    def __init__(self):
        self.root = None
        self.k = 0

    def book(self, start, end, root, count):
        if not root:
            root = BstNode(start, end, count)
            self.k = max([self.k, root.count])
        elif start >= root.end:
            root.right = self.book(start, end, root.right, count)
        elif end <= root.start:
            root.left = self.book(start, end, root.left, count)
        else:
            min_start = min([start, root.start])
            max_start = max([start, root.start])
            min_end = min([end, root.end])
            max_end = max([end, root.end])

            if min_start < max_start:
                root.left = self.book(min_start, max_start, root.left, count if start < root.start else root.count)

            if min_end < max_end:
                root.right = self.book(min_end, max_end, root.right, count if end > root.end else root.count)

            root.start = max_start
            root.end = min_end
            root.count += count
            self.k = max([self.k, root.count])
        return root


class BstNode:
    def __init__(self, start, end, count, left=None, right=None):
        self.start = start
        self.end = end
        self.count = count
        self.left = left
        self.right = right

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)


def solution(inputs):
    obj = MyCalendarThree()
    for input in inputs:
        print(obj.book(*input))


solution([[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]])