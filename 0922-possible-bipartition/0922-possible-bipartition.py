class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i , j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        
        colors = {}

        def dfs(node,color):
            if node in colors:
                return colors[node] == color

            colors[node] = color

            for n in graph[node]:
                if not dfs(n, 1-color):
                    return False
            
            return True

        
        for i in range(len(graph)):
            if i not in colors:
                if not dfs(i,0):
                    return False
        return True