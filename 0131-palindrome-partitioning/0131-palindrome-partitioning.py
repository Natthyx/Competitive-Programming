class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(word):
            return word == word[::-1]
        res = []
        path = []

        def backtracking(i):
            if i >= len(s):
                res.append(path[:])
                return
            
            for j in range(i,len(s)):
                if helper(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtracking(j+1)
                    path.pop()
        
        backtracking(0)
        return res