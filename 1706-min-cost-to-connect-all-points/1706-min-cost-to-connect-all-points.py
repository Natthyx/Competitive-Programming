class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''

        - connect each point with all other than itself
        - use min_heap to find the smallest distance, everytime we select one path, the reverse should be visited
        - iterate through the points and sum up the smallest weight in to the ans


        '''

        # build the graph with weight
        graph = []
        for i in range(len(points)):
            for j in range(i,len(points)):
                if points[j] == points[i]:
                    continue
                weight = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                heapq.heappush(graph,[weight,tuple(points[i]),tuple(points[j])])
        
        
        parents = {tuple(points[i]) : tuple(points[i]) for i in range(len(points))}
        size = {tuple(points[i]) : 1 for i in range(len(points))}

        def find(point):
            if point != parents[point]:
                parents[point] = find(parents[point])
            
            return parents[point]

        def union(x,y):
            findx = find(x)
            findy = find(y)

            if findx == findy:
                return False
            
            if size[findx] > size[findy]:
                parents[findy] = findx
                size[findx] += size[findy]
            else:
                parents[findx] = findy
                size[findy] += size[findx]

            return True
        

        ans = 0
        edge = 0
        while graph:
            if edge == len(points)-1:
                break
            w , x ,y = heapq.heappop(graph)
            
            if union(x,y):
                ans+=w
    
        return ans

            






