class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.val = value
        self.k = k
        self.dict = defaultdict(int)
        self.unique = 0
    
    

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if self.dict[num]==0:
            self.unique+=1

        self.dict[num]+=1

        if len(self.queue) < self.k:
            return False
                
        elif len(self.queue) == self.k:
            if self.unique == 1 and num==self.val:
                return True
            else:
                return False
        
        elif len(self.queue) > self.k:
            a = self.queue.popleft()
            self.dict[a]-=1
            if self.dict[a]==0:
                self.unique-=1
            if self.unique == 1 and num==self.val:
                return True
            else:
                return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)