class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {"+","-","*","/"}

        
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                if stack and len(stack) > 1:
                    b = stack.pop()
                    a = stack.pop()

                if tokens[i] == "+":
                    ans = a+b
                elif tokens[i] == "-":
                    ans = a-b
                elif tokens[i]=="*":
                    ans = a*b
                elif tokens[i] == "/":
                    ans = int(a/b)
            
                stack.append(ans)
        return stack[0]

                
