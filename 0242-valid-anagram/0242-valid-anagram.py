class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        forS = Counter(s)
        forT = Counter(t)
        if forS == forT:
            return True
        
            
        
        