
class Point:
    def __init__(self, node):
        self.current = node
        self.history = []

    def up(self, n):
        for _ in range(0, n):
            if self.current.up:
                self.current = self.current.up
            else:
                return

    def down(self, n):
        for _ in range(0, n):
            if self.current.down:
                self.current = self.current.down
            else:
                return

    def delete(self):
        down = self.current.down
        up = self.current.up
        if down:
            down.up = up
        if up:
            up.down = down
        self.history.append((up, self.current, down))
        self.current = down if self.current.down else up

    def undo(self):
        up, deleted, down = self.history.pop()
        if up:
            up.down = deleted
        if down:
            down.up = deleted

    def get_answer(self, n):
        answer = ['X'] * n
        self.up(n)
        for i in range(n):
            value = self.current.value
            answer[value] = 'O'
            if self.current.down:
                self.current = self.current.down
            else:
                return ''.join(answer)

class Node:
    def __init__(self, value, up=None, down=None):
        self.up = up
        self.down = down
        self.value = value


def solution(n, k, cmd):
    nodes = [Node(value=i) for i in range(n)]
    for i in range(n):
        if i == 0:
            nodes[i].down = nodes[i+1]
        elif i == n-1:
            nodes[i].up = nodes[i-1]
        else:
            nodes[i].up = nodes[i-1]
            nodes[i].down = nodes[i+1]

    point = Point(nodes[k])

    for command in cmd:
        if command[0] == 'C':
            point.delete()
        elif command[0] == 'Z':
            point.undo()
        else:
            direction, num = command.split(' ')
            print(direction, num)
            if direction == 'D':
                point.down(int(num))
            else:
                point.up(int(num))

    return point.get_answer(n)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	))

