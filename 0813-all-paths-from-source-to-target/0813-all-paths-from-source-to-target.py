class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stack = [0]

        def dfs(ind):
            if ind == len(graph)-1:
                ans.append(stack[:])
                return
            
            for i in graph[ind]:
                stack.append(i)
                dfs(i)
                stack.pop()
        
        dfs(0)
        return ans


            
