class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graphs = defaultdict(list)
        out_degree = [0]*len(graph)
        res = []
        # construct the graph and also store the out_degree
        for i in range(len(graph)):
            for node in graph[i]:
                graphs[node].append(i)
                out_degree[i]+=1
        queue = deque()
        for i in range(len(graph)):
            # appen to the only those who don't have an out_degree(out_degree = 0)
            if out_degree[i] == 0:
                queue.append(i)

        while queue:
            # append them in res
            node = queue.popleft()
            res.append(node)

            for n in graphs[node]:
                # deduct the parent out_degree from the children
                out_degree[n]-=1
                if out_degree[n] == 0:
                    queue.append(n)

        return sorted(res)             