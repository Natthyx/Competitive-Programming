class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [set() for _ in range(n)]
        graph = defaultdict(list)
        for a , b in edges:
            graph[a].append(b)

        
        def dfs(node, a):
            for n in graph[node]:
                if a not in res[n]:
                    res[n].add(a)
                    dfs(n,a)
        
        for i in range(n):
            dfs(i,i)
        
        return [sorted(list(a)) for a in res]
