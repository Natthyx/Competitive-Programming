class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "c":
                if len(stack)>=2 and stack[-1] =="b" and stack[-2]=="a":
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return not stack 
        