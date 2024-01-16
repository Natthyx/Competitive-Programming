import random
class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.currentSet = set()
        

    def insert(self, val: int) -> bool:
        if val in self.currentSet:
            return False
        
        self.lst.append(val)
        self.currentSet.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.currentSet:
            return False
        
        self.currentSet.remove(val)
        index = self.lst.index(val)
        self.lst[index], self.lst[-1] = self.lst[-1] , self.lst[index]
        self.lst.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()