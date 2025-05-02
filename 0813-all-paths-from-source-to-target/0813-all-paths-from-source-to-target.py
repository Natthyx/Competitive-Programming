class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stack = [0]
        def dfs(i):
            if i == len(graph)-1:
                ans.append(stack[:])
                return
            
            for n in graph[i]:
                stack.append(n)
                dfs(n)
                stack.pop()

        dfs(0)
        return ans

            
