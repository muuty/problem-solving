
from collections import deque


def check(word1, word2):
    same = [0 if word1[i] == word2[i] else 1 for i in range(len(word1))] 
    if sum(same) == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    q = deque()
    visited = [0]*len(words)

    q.append((begin, 0))
    word, number = 0, 0
    while len(q) > 0:
        word, number = q.popleft()
        if word == target:
            return number
        for i in range(len(words)):
            if visited[i] != True and check(word, words[i]):
                visited[i] = True
                q.append((words[i], number + 1))
            
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))