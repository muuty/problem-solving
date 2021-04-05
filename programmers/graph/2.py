
class Node:
    def __init__(self, value):
        self.value = value
        self.left = {}
        self.right = {}
        self.left_nodes = -1
        self.right_nodes = -1
        self.left_count = -1
        self.right_count = -1

    def get_left_nodes(self):
        if self.left_nodes == -1:
            self.left_nodes = {}
            if self.left:
                self.left_nodes = {}

                for key in self.left:
                    self.left_nodes[key] = True
                    self.left_nodes.update(self.left[key].get_left_nodes())

        return self.left_nodes

    def get_right_nodes(self):
        if self.right_nodes == -1:
            self.right_nodes = {}
            if self.right:
                self.right_nodes = {}
                for key in self.right:
                    self.right_nodes[key] = True
                    self.right_nodes.update(self.right[key].get_right_nodes())

        return self.right_nodes


    def append_left(self, node):
        self.left[node.value] = node

    def append_right(self, node):
        self.right[node.value] = node

def solution(n, results):
    nodes = [Node(i) for i in range(1, n+1)]

    for result in results:
        nodes[result[0]-1].append_right(nodes[result[1]-1])
        nodes[result[1]-1].append_left(nodes[result[0]-1])

    answer = 0



    for node in nodes:
        if len(node.get_left_nodes()) + len(node.get_right_nodes()) == n-1:
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	 ))