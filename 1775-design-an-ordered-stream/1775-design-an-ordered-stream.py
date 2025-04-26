class OrderedStream:

    def __init__(self, n: int):
        self.stream = ["" for _ in range(n+1)]
        self.ptr = 1

        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey]+=value
        res = []
        while self.ptr < len(self.stream):
            if self.stream[self.ptr] != "":
                res.append(self.stream[self.ptr])
                self.ptr+=1
            else:
                break
        
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)