class Solution:
    def isValid(self, s: str) -> bool:
        brace = {
            "}":"{",
            "]":"[",
            ")":"("}

        stack = []

        for i in s:
            if i not in brace:
                stack.append(i)

            elif i in brace:
                if not stack:
                    return False
                elif stack and stack[-1] == brace[i]:
                    stack.pop()
                elif stack and stack[-1] != brace[i]:
                    return False
                
        if stack:
            return False
        else:
            return True


        