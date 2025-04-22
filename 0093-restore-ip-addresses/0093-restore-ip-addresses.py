class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        store = []
        

        def backtrack(ind):
            if ind == len(s):
                return
            if len(store) == 3:
                temp = s[ind:]
                flag = int(temp) <= 255
                if len(temp) > 1 and temp[0] =="0":
                    flag = False
                for ip in store:
                    if len(ip) > 1 and ip[0]=="0":
                        flag = False
                    if int(ip) > 255:
                        flag = False
                
                if flag:
                    store.append(s[ind:])

                    res.append(".".join(store))
                    store.pop()
                return

            for j in range(ind,len(s)):
                store.append(s[ind:j+1])
                backtrack(j+1)
                store.pop()
        
        backtrack(0)
        return res
            
                

            




           


