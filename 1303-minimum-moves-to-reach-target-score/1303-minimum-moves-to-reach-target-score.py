class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        if maxDoubles == 0:
            return target-1
        
        while maxDoubles > 0 and target != 1:
            if target % 2 == 0:
                target//=2
                maxDoubles-=1
            else:
                target-=1
            
            count+=1            

        if target == 1:
            return count
        else:
            return count+ (target-1)
