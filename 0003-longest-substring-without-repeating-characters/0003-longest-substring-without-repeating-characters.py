class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        count = defaultdict(int)
        left = 0
        n = len(s)
        maxS = 0
        for right in range(n):
            
            count[s[right]] +=1
            
            while count[s[right]] >1 and left <= right:
                count[s[left]]-=1
                left+=1
            maxS = max(right-left+1,maxS)
        return maxS
                
            
        
        