class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_sm = 0
        current_sm = 0
        freq = {}
        
        for i in nums:
            current_sm+=i
            
            if current_sm == goal:
                total_sm+=1
            
            
            if current_sm - goal in freq:
                total_sm += freq[current_sm -goal]
                
            freq[current_sm] = freq.get(current_sm,0)+1
            
        return total_sm
                
                