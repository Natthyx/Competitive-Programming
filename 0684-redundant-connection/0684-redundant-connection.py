class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        size = [1] * (len(edges)+1)
        ans = None
        
        def find(x):
            if x == parent[x]:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            findx = find(x)
            findy = find(y)
            
            if findx != findy:
                if size[findx] > size[findy]:
                    parent[findy] = findx
                    size[findx] += size[findy]
                else:
                    parent[findx] = findy
                    size[findy] += size[findx]

        for edge in edges:
            a , b = edge
            if find(a) == find(b):
                ans = [a,b]
            
            union(a,b)
        
        return ans