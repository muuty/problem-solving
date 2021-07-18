import random

class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sets = {}
        self.positions = {}
        self.n = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.sets:
            self.sets[val] = set()
            self.sets[val].add(self.n)
            self.positions[self.n] = val
            self.n += 1
            return True
        else:
            self.sets[val].add(self.n)
            self.positions[self.n] = val
            self.n += 1
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.sets:
            return False

        val_index = self.sets[val].pop()
        if not self.sets[val]:
            self.sets.pop(val)

        if val_index != self.n - 1:
            change_val = self.positions[self.n - 1]
            self.sets[change_val].remove(self.n - 1)
            self.sets[change_val].add(val_index)
            self.positions[val_index] = change_val

        self.n -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.positions[random.randint(0, self.n - 1)]


