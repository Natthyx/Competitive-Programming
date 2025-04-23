class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        graph = defaultdict(list)
        intake = [0]*numCourses

        for a , b in prerequisites:
            graph[b].append(a)
            intake[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if intake[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            res.append(node)

            for n in graph[node]:
                intake[n] = max(intake[n]-1, 0)

                if intake[n] == 0:
                    queue.append(n)
        
        if len(res) == numCourses:
            return res
        else:
            return []
        








