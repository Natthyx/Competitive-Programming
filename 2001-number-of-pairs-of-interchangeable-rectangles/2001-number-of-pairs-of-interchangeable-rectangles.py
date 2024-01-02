class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        result = {}
        count = 0
        for w,h in rectangles:
            ratio = w/h
            if ratio in result:
                result[ratio]+=1
                count += result[ratio]
            else:
                result[ratio]=0
        return count
            
            
                
            
        