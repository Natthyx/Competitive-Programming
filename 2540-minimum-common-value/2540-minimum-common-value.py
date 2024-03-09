class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        res = float("inf")
        for key in counter1.keys():
            if key  in counter2.keys():
                res = min(res,key)
                return res
                
        return -1
            
                
        