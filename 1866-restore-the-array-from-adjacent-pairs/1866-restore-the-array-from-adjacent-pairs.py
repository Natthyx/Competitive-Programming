class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        queue = deque()
        visited = set()
        ans = []
        graph = defaultdict(list)

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        
        for key,val in graph.items():
            if len(val) == 1:
                queue.append(key)
                break
            

        while queue:
            val = queue.popleft()
            if val in visited:
                continue
            visited.add(val)
            ans.append(val)
            for n in graph[val]:
                if n not in visited:
                    queue.append(n)

        return ans





        
        