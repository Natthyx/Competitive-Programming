class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        s.sort()
        n = len(s)
        ans = s[:n-1]

        ans.sort(reverse=True)

        ans = "".join(ans)
        ans+="1"
        return ans
        