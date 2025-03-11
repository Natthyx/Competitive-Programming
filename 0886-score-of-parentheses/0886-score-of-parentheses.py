class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in range(len(s)):
            if s[i] =="(":
                stack.append(0)

            else:
                a = stack.pop()
                op = max(a*2,1)

                stack[-1]+=op

        return stack[-1]

