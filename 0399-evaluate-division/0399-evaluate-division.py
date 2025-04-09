class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for i in range(len(equations)):
            x , y = equations[i]
            graph[x].append([y,values[i]])
            graph[y].append([x,(1/values[i])])
        
        
        def dfs(node,target,visited, path):
            if node == target:
                ans.append(path)

            visited.add(node)
            for n, v in graph[node]:
                if n not in visited:
                    dfs(n,target,visited,path*v)

        ans = []

        for node, val in queries:
            visited = set()
            if node not in graph:
                ans.append(-1.0)
                continue
            dfs(node,val,visited,1)
            if val not in visited:
                ans.append(-1.0)
            
        
        return ans
        