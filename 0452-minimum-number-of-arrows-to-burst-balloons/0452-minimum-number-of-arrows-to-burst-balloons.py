class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])
        ans = 1
        start, j = points[0][1] , 0
        
        while j < len(points):
            if points[j][0] > start:
                ans+=1
                start = points[j][1]

            j+=1
        return ans