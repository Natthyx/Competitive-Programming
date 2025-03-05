class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicts = { "(":")", "[":"]","{":"}"}

        for brace in s:
            if brace in dicts:
                stack.append(brace)
            else:
                if not stack:
                    return False

                a = stack.pop()
                if brace != dicts[a]:
                    return False
        return stack == []

        
        