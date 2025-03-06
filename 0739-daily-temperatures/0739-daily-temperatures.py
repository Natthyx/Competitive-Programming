class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0]*len(temp)
        stack = []
        day = defaultdict(int)

        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                a = stack.pop()
                ans[a] = i-a
            else:
                stack.append(i)

        return ans

