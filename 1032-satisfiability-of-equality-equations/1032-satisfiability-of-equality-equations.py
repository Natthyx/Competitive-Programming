class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {i:i for i in range(26)}

        size = [1] * (26)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]

        def union(x,y):
            findx = find(x)
            findy = find(y)

            if findx == findy:
                return False
            
            if size[findx] > size[findy]:
                parent[findy] = findx
                size[findx] += size[findy]

            else:
                parent[findx] = findy
                size[findy] += size[findx]
            
            return True

        
        for ch1 , op1 , op2, ch2 in equations:
            a = ord(ch1) - ord("a")
            b = ord(ch2) - ord("a")
            if op1 == "=":
                union(a,b)
            
        for ch1 , op1 , op2, ch2 in equations:
            a = ord(ch1) - ord("a")
            b = ord(ch2) - ord("a")
            if op1 == "!":
                if find(a) == find(b):
                    return False
                

        return True


