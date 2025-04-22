class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opn,close,store):
            if opn == close == n:
                res.append("".join(store))
                return
            
            if opn < n:
                store.append("(")
                backtrack(opn+1, close, store)
                store.pop()
            if close < opn:
                store.append(")")
                backtrack(opn,close+1,store)
                store.pop()
        backtrack(0,0,[])
        return res