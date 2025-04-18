class RandomizedSet:

    def __init__(self):
        self.randomizedset = defaultdict(int)
        self.arr = []
         

    def insert(self, val: int) -> bool:
        if val not in self.randomizedset:
            self.randomizedset[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False
        
        

    def remove(self, val: int) -> bool:
        if val in self.randomizedset:
            last = self.arr[-1]
            ind = self.randomizedset[val]
            self.arr[ind] = last
            self.arr.pop()

            self.randomizedset[last] = ind
            del self.randomizedset[val]
            return True
        else:
            return False
        
        

    def getRandom(self) -> int:
        return random.choice(self.arr)

        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()