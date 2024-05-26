class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res, broken = 0, set(brokenLetters)
        for w in text.split():
            if not set(w) & broken:
                res += 1
        return res
        
        