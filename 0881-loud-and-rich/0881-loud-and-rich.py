class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        in_degre = [0]*len(quiet)

        res = [i for i in range(len(quiet))]

        for x, y in richer:
            graph[x].append(y)
            in_degre[y] += 1
        
        queue = deque()
        for i in range(len(quiet)):
            if in_degre[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()

            for n in graph[node]:
                if quiet[res[node]] < quiet[res[n]]:
                    res[n] = res[node]
                in_degre[n]-=1
                if in_degre[n] == 0:
                    queue.append(n)
        
        return res