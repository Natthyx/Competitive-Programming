class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxNo =  defaultdict(int)
        i = lowLimit
        
        while i <= highLimit:
            temp = list(str(i))
            sumof = sum(int(x) for x in temp)
            boxNo[sumof]+=1
            i+=1
            
        return max(boxNo.values())
                
            