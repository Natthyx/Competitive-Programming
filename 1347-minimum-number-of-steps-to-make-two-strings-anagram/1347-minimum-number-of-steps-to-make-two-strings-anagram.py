class Solution:
    def minSteps(self, s: str, t: str) -> int:
        charOfS = {}
        charOfT = {}
        result = 0
        for i in s:
            charOfS[i] = charOfS.get(i,0)+1
        for i in t:
            charOfT[i] =  charOfT.get(i,0)+1
        
        for key, value in charOfS.items():
            if key in charOfT:
                if value == charOfT[key]:
                    result += value
                else:
                    result += min(value,charOfT[key])
        return len(s) - result
                    
        
        
        
        