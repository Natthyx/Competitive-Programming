class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = []

        for i in range(len(s)):
            s[i] = (s[i][:-1],int(s[i][-1]))
        
        s.sort(key = lambda x: x[1])
        
        for i in range(len(s)):
            ans.append(s[i][0])
        
        return " ".join(ans)


