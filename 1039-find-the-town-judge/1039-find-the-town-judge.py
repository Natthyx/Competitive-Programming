class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        ind = [0] * (n+1)
        out = [0] * (n+1)
        for x,y in trust:
            graph[x].append(y)
            ind[y]+=1
            out[x]+=1

        for person in range(1,n+1):
            if ind[person] == n-1 and out[person]==0:
                return person
        return -1

        

        