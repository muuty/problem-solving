import collections

class WordDictionary(object):
    def __init__(self):
        self.dict = collections.defaultdict(set)

    def addWord(self, word):
        self.dict[len(word)].add(word)

    def search(self, word):
        if '.' not in word:
            return word in self.dict[len(word)]
        for cand in self.dict[len(word)]:
            found = True
            for i in range(len(cand)):
                if cand[i] != word[i] and word[i] != '.':
                    found = False
                    break
            if found:
                return True
        return False