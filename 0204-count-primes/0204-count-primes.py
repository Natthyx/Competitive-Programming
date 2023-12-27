class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n==1: return 0
        prime = [True]*n
        prime[0], prime[1]= False , False
        arr = []
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for x in range(i*i,n,i):
                    prime[x]=False
        for i in range(2,n):
            if prime[i]:
                arr.append(i)

        return len(arr)





        
            

        

        