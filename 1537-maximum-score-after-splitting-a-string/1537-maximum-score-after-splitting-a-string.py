class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0]*(len(s))
        pre = 0


        for r in range(len(s)):
            pre += int(s[r])
            prefix[r] = pre

        mx = 0
        for i in range(len(prefix)-1):
            zeros = i - prefix[i]+1
            one = prefix[-1]- prefix[i]

            mx = max(mx,(zeros+one))

        return mx


