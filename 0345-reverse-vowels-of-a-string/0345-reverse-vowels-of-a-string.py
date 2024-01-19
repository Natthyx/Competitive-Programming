class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["a","e","i","o","u"]
        s = list(s)
        i = 0
        j = len(s)-1
        
        while i < j:
            while i < j and s[i].lower() not in vowel:
                i+=1
            while i< j and s[j].lower() not in vowel:
                j-=1
            
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return ''.join(s)
        