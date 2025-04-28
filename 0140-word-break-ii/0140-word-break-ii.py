class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict) # O(1) look-up
        
        curr = []
        res = []
        def backtrack(i):
            # base case
            if i == len(s):
                res.append(" ".join(curr))
                return
            
            # iterate on the string starting from the index
            for j in range(i,len(s)):
                word = s[i:j+1]
                # check if the word is in wordDict
                if word in wordDict:
                    curr.append(word)
                    backtrack(j+1)
                    curr.pop()
        
        backtrack(0)
        return res
