class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        size = [1] * len(accounts)
        def find(x):
            if x == parent[x]:
                return parent[x]
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

        
        emailsToAcc = {}

        for i , a in enumerate(accounts):
            for e in a[1:]:
                if e in emailsToAcc:
                    union(i, emailsToAcc[e])
                else:
                    emailsToAcc[e] = i

        
        emailGroup = defaultdict(list)

        for key , val in emailsToAcc.items():
            leader = find(val)
            emailGroup[leader].append(key)
        
        res = []

        for key , val in emailGroup.items():
            name = accounts[key][0]
            res.append([name] + sorted(emailGroup[key]))

        return res
