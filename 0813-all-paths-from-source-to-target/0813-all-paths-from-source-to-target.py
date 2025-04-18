class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(node,stack):

            if node == len(graph)-1:
                ans.append(stack[:])
                return

            for i in graph[node]:
                stack.append(i)
                dfs(i,stack)
                stack.pop()

        dfs(0,[0])
        return ans
        