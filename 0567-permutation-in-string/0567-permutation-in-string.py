class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        anagram = Counter(s1)
        first = Counter(s2[:n])
        
        if anagram == first:
            return True
        left = 0
        for right in range(n, len(s2)):
            first[s2[left]]-=1
            if first[s2[left]]==0:
                del first[s2[left]]
            left+=1
            first[s2[right]]+=1
            if anagram == first:
                return True
            
            
        