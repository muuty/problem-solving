from collections import defaultdict

class Node:
    def __init__(self):
        self.data = dict()
        self.trace = ''
        self.finished = False

def solution(words, queries):
    head = Node()
    for word in words:
        node = head
        for i in range(0, len(word)):
            if word[i] not in node.data:
                node.data[word[i]] = Node()
                node.data[word[i]].trace = node.trace + word[i]
            node = node.data[word[i]]
        node.finished = True


    answer = []
    for query in queries:
        stack = [head]
        count = 0
        stack = [[head, 0]]
        while stack:
            node, i = stack.pop()
            print(node.trace)
            if i == len(query):
                if node.finished:
                    count += 1
                continue
            if query[i] == '?':
                if node.data:
                    for next_node in node.data.values():
                        stack.append([next_node, i+1])

            else:
                if query[i] in node.data:
                    stack.append([node.data[query[i]], i + 1])
        answer.append(count)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"]	,["fro??", "????o", "fr???", "fro???", "pro?"]		))