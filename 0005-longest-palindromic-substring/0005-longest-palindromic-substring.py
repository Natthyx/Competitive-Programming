class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for start in range(len(s)):
            end = start + 1

            while end < len(s):
                string = s[start:end+1]
                revStr = string[::-1]
                if string == revStr:
                    if len(ans) < len(string):
                        ans = string
                
                end += 1
        
        if len(ans) == 0:
            return s[0]
        return ans
        