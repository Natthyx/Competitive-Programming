class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        def dfs(v,visited):
            if v == destination:
                return True

            visited.add(v)
            for n in graph[v]:
                if n not in visited:
                    if dfs(n,visited):
                        return True

            return False

        return dfs(source,set())

        