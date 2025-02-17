# https://leetcode.com/problems/insert-delete-getrandom-o1/


# Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements.
# Each element must have the same probability of being returned.


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.list = list()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        else:
            self.map[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            # replace deleted one with tail
            index = self.map[val]
            tail = self.list.pop()
            if index < len(self.list):
                self.list[index] = tail
                self.map[tail] = index
            del self.map[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
