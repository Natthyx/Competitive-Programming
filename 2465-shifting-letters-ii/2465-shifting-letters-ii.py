class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)
        ans = ''
        for start,end,d in shifts:
            if d == 0:
                prefix[start]-=1
                prefix[end+1]+=1
            else:
                prefix[start]+=1
                prefix[end+1]-=1

        for i in range(1,len(prefix)):
            prefix[i]+= prefix[i-1]

        for i in range(len(s)):
            order = ord(s[i])-ord('a')
            mods = (order+prefix[i])%26
            ans += chr(mods+ord('a'))
            

        return ans







        