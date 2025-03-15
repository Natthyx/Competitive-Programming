class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def mod_expo(base,k,mod):
            ans = 1
            while k > 0:
                if k % 2 == 1:
                    ans = (ans*base)%mod
                base = (base**2)%mod
                k//=2
            return ans
        
        mod = (10**9)+7
        return (mod_expo(5,(n+1)//2,mod)*(mod_expo(4,n//2,mod)))%mod