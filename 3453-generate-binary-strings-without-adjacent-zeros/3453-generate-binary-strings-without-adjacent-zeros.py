class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(i, store):
            if i == n:
                ans.append("".join(store[:]))
                return
            
            if store and store[-1] == "0":
                store.append("1")
                backtrack(i+1,store)
                store.pop()
                    
            else:
                store.append("1")
                backtrack(i+1,store)
                store.pop()
                store.append("0")
                backtrack(i+1,store)
                store.pop()

        backtrack(0,[])
        return ans
