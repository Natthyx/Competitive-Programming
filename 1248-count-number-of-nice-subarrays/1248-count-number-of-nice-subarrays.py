class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int: 
#         prefixum
        prefix = {0:1}
        sm = 0
        res= 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        for i in range(len(nums)):
            sm+=nums[i]
            dif = sm-k
            res+= prefix.get(dif,0)
            prefix[sm]= prefix.get(sm,0)+1
        return res
            
            
            
#         two pointer       
#         odd = 0
#         left = 0
#         ans = 0
#         res =0
#         for right in range(len(nums)):
#             if nums[right] % 2 == 1:
#                 odd+=1
#                 ans= 0
            
#             while odd == k:
#                 if nums[left] % 2 == 1 :
#                     odd-=1
#                 ans+=1
#                 left+=1
                
#             res+=ans
#         return res

                
        
                