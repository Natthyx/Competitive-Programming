class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def div_conq(string):
            for i in range(len(string)):
                if string[i].swapcase() not in string:
                    left = div_conq(string[:i])
                    right = div_conq(string[i+1:])

                    if len(left) >= len(right):
                        return left
                    else:
                        return right
            
            return string

        return div_conq(s)

