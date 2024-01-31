class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        N = len(name)
        V = len(typed)
        flag = True

        r = 0

        if len(typed) < len(name):
            return False

        for l in range(N):
            if name[l] not in typed[r:]:
                return False
            if name[l] != typed[r]:
                print(l,r)
                flag = False
                break
            else:
                if l< N-1 and name[l+1] == name[l]:
                    r+=1
                else:
                    while  r<V and typed[r] == name[l]:
                        r+=1
            
        print(r)
        if typed[r:].count(name[-1]) != V-r:
            flag = False
        return flag