class Solution:
    def decodeString(self, s: str) -> str:
        num_set = set(map(str, range(0, 301)))
        stack = []
        for i in range(len(s)-1,-1,-1):
            if s[i] == "[":
                j = i-1
                a = ""
                if s[j] not in num_set:
                    a = "1"
                else:
                    while j > -1 and s[j] in num_set:
                        a = s[j] + a
                        j-=1

                a = int(a)  
                ch = ''
                while stack and stack[-1] != "]":
                    ch +=stack.pop()
                stack.pop()
                stack.append(a*ch)

            elif s[i] in num_set:
                continue
            else:
                stack.append(s[i])
        
        return "".join(stack[::-1])



