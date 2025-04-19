class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        
        queue = deque()
        queue.append((headID,0))
        mx = 0
        while queue:
            node,time = queue.popleft()
            mx = max(mx,time)

            for n in graph[node]: 
                queue.append((n, time + informTime[node]))
            

        return mx

        
        