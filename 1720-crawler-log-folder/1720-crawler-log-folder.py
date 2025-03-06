class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        change = 0

        for i in range(len(logs)):
            if logs[i] != "../" and logs[i] != "./":
                stack.append(1)
            elif stack and logs[i] == "../":
                stack.pop()
            

        return len(stack)
            
            

