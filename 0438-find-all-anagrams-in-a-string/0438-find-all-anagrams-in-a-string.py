class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        res = []
        anagrams = Counter(p)
        first = Counter(s[:n])
        left = 0
        if anagrams == first:
                res.append(left)
        for right in range(n, len(s)):
            first[s[left]]-=1
            if first[s[left]] == 0:
                del first[s[left]]
            left+=1
            first[s[right]] +=1
            if anagrams == first:
                res.append(left)
            
            
        return res
        
        
            
            
        
        