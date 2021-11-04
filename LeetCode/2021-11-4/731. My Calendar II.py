class MyCalendarTwo(object):
    def __init__(self):
        self.tree = BST()

    def book(self, start, end):
        self.tree.is_booked = True
        self.tree.root = self.tree.book(start, end, self.tree.root, 1)
        return self.tree.is_booked


class BST:
    def __init__(self):
        self.root = None
        self.is_booked = True

    def book(self, start, end, root, count):
        if not root:
            root = BstNode(start, end, count)
            self.is_booked = True
        elif start >= root.end:
            root.right = self.book(start, end, root.right, count)
        elif end <= root.start:
            root.left = self.book(start, end, root.left, count)
        else:
            if root.count + count < 3:
                min_start = min([start, root.start])
                max_start = max([start, root.start])
                min_end = min([end, root.end])
                max_end = max([end, root.end])

                if min_start < max_start:
                    root.left = self.book(min_start, max_start, root.left, count if start < root.start else root.count)
                    if not self.is_booked:
                        return root

                if min_end < max_end:
                    root.right = self.book(min_end, max_end, root.right, count if end > root.end else root.count)
                    if not self.is_booked:
                        return root

                root.start = max_start
                root.end = min_end
                root.count += count
            else:
                self.is_booked = False

        return root


class BstNode:
    def __init__(self, start, end, count, left=None, right=None):
        self.start = start
        self.end = end
        self.count = count
        self.left = left
        self.right = right


def solution(inputs):
    obj = MyCalendarTwo()
    for input in inputs:
        print(obj.book(*input))


solution([[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]])