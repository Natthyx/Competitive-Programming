class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        
        points.sort(key=lambda x : x[1])
        
        start =points[0][1]
        
        for i in range(1,len(points)):
            if points[i][0] > start:
                res+=1
                start = points[i][1]
        return res
                
        