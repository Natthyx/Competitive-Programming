class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 10**9 + 7

        stack = []
        ans = 0

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                ans = (ans + arr[j] * left * right) % M

            stack.append(i)

        
        for i in range(len(stack)):
            j = stack[i]
            left = j - stack[i-1] if i > 0 else j + 1
            right = len(arr) - j
            ans = (ans + arr[j] * left * right) % M

        return ans




        
