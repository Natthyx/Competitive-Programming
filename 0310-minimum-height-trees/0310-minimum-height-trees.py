class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        arr = [0]*n

        if n == 1:
            return [0]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque()

        for node in range(n):
            arr[node] = len(graph[node]) - 1
            if not arr[node]:
                queue.append(node)

        ans = []

        while queue:
            ans = list(queue)
            child = len(queue)

            for _ in range(child):
                node = queue.popleft()

                for nei in graph[node]:
                    arr[nei] -= 1
                    if not arr[nei]:
                        queue.append(nei)
        
        return ans