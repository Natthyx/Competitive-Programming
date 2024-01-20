class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res= []
        def rec(comb, strs):
            if len(strs)==0:
                res.append(comb)
            else:
                for i in d[strs[0]]:
                    rec(comb+i, strs[1:])
        
        if digits:
            rec('',digits)
        return res