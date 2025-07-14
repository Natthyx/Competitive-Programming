class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        - we have two choice for each time, if we take it or if we don't take it
        - if we take it: we will find the index that is not overlap with the current one and do same backtracking for it
        - if we don't take it: we will check for the next interval

        '''
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            # base case
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            # don't include
            res = dfs(i+1)

            # include
            # we gonna find the next index that is not going to overlap
            j = bisect.bisect(intervals, (intervals[i][1],-1,-1))
            res = max(res , intervals[i][2]+ dfs(j))
            cache[i] = res
            return res
        
        return dfs(0)





        