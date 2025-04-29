class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        res = []
        is_reachable = [set() for _ in range(numCourses)]

        for prev , curr in prerequisites:
            graph[prev].append(curr)
            in_degree[curr] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                is_reachable[nei].add(node)
                is_reachable[nei].update(is_reachable[node])
                in_degree[nei]-=1
                if in_degree[nei] == 0:
                    queue.append(nei)
            

        for i , j in queries:
            if i in is_reachable[j]:
                res.append(True)
            else:
                res.append(False)
        
        return res     

