class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        change = 0

        for i in range(len(logs)): 
            if logs[i] == "../":
                if stack:
                    stack.pop()
                    
            elif logs[i] == "./":
                continue
            else:
                stack.append(1)
            

        return len(stack)
            
            

