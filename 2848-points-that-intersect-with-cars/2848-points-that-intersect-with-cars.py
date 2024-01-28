class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        hashmap = {}
        for start, end in nums:
            while start <= end:
                hashmap[start] = hashmap.get(start,0)+1
                start+=1
        res = len(hashmap)
        
        return res
                
        