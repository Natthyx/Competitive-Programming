class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.ind = 0
        self.isZero = False


    def add(self, num: int) -> None:
        if num == 0:
            self.ind = 1
            self.isZero = True
            self.prefix.append(1)
        else:
            if self.isZero:
               self.ind += 1 
            self.prefix.append(self.prefix[-1] * num)


    def getProduct(self, k: int) -> int:
        if self.isZero and self.ind <= k:
            return 0
        else:
            return self.prefix[-1] // self.prefix[-k-1]
        
        
        

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)