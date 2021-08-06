NODE_FINISHED = "FINISHED"

class Node():
    def __init__(self, value=None):
        self.val = value
        self.children = {}
        self.finished = False

    def add_child(self, value):
        if value not in self.children:
            self.children[value] = Node(value)

    def get_child(self, value):
        if value in self.children:
            return self.children[value]
        else:
            return None

    def get_every_child(self):
        return list(self.children.values())

    def set_finish(self):
        self.finished = True

    def is_finished(self):
        return self.finished


class WordDictionary(object):
    def __init__(self):
        self.root = Node()
        self.dict = {}

    def addWord(self, word):
        recent_node = self.root
        for i in range(len(word)):
            recent_node.add_child(word[i])
            recent_node = recent_node.get_child(word[i])
        recent_node.set_finish()

    def search(self, word):
        current_nodes = [self.root]
        for i in range(len(word)):
            new_nodes = []
            if word[i] == '.':
                for node in current_nodes:
                    new_node = node.get_every_child()
                    if new_node:
                        new_nodes += new_node
                current_nodes = new_nodes
            else:
                for node in current_nodes:
                    new_node = node.get_child(word[i])
                    if new_node:
                        new_nodes.append(new_node)
                current_nodes = new_nodes

        for node in current_nodes:
            if node.is_finished():
                return True
        return False


dictonary = WordDictionary()
dictonary.addWord("at")
dictonary.addWord("an")
dictonary.addWord("and")
dictonary.addWord("add")

print(dictonary.search("a"))
#print(dictonary.search("a"))
#print(dictonary.search("aa"))
#print(dictonary.search(".a"))
#print(dictonary.search("a."))
