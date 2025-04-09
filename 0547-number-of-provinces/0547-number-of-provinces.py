class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(1,len(isConnected)+1):
            for j in range(0,len(isConnected[i-1])):
                if isConnected[i-1][j]==1:
                    graph[i].append(j+1)

        visited = set()

        def dfs(node):

            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    dfs(n)
            
        count = 0
        for i in graph:
            if i not in visited:
                count+=1
                dfs(i)

        return count



            