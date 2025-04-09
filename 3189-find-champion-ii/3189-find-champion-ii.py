class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])

        visited = set()
        def dfs(node):
            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    dfs(n)
        
        keys = list(graph.keys())

        for i in range(n):
            if i not in visited:
                visited = set()
                dfs(i)
                if len(visited)== n:
                    return i

        return -1

