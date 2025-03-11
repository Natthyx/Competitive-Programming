class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0

        for i in range(len(s)):
            if s[i] =="(":
                stack.append(s[i])

            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append(1)

                elif stack and stack[-1] != "(":
                    x = 0
                    while stack and stack[-1] != "(":
                        x+=stack.pop()

                    stack.pop()
                    stack.append(x*2)

        return sum(stack)

