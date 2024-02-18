class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ["a","A","e","E","i","I","o","O","u","U"]
        s = sentence.split()
        a = "a"
        for i in range(len(s)):
            if s[i][0] in vowel:
                s[i]=s[i]+"ma"+(i+1)*a
            elif s[i][0] not in vowel:
                s[i] = s[i][1:]+s[i][:1]+"ma"+(i+1)*a
                
        sentence = " ".join(s)
        return sentence