class Solution:
    def fib(self, n: int) -> int:
        def fn(n):
            if n <=1:
                return n
            else:
                return fn(n-1) + fn(n-2)
        
        return fn(n)
            
        
        
        