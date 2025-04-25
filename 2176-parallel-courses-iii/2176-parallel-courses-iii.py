class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int: 
        graph = defaultdict(list)
        in_degree = [0]*(n+1) 
        times = [0]*(n+1)
        for x , y in relations:
            graph[x].append(y)
            in_degree[y]+=1

        
        queue = deque()
        for i in range(1,n+1):
            times[i] = time[i-1]
            if in_degree[i]==0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            
            for n in graph[node]:
                in_degree[n] -= 1
                times[n] = max(times[n], times[node]+time[n-1])
                if in_degree[n] == 0:
                    queue.append(n)
        
        
        return max(times)
