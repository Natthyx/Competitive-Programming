class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        wordDict = set(words)
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]

            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if ((prefix in wordDict and suffix in wordDict) or (prefix in wordDict and dfs(suffix))):
                    dp[word] = True
                    return dp[word]
            
            dp[word] = False
            return dp[word]
        
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res
                
