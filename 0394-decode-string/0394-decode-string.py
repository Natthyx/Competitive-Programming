class Solution:
    def decodeString(self, s: str) -> str:
        def helper(ind):
            res = ''
            num = 0

            while ind < len(s):
                char = s[ind]

                # first if it is [
                if char == '[':
                    decoded , ind = helper(ind+1)
                    res += decoded*num
                    num = 0
                
                # second if it is ]
                elif char == ']':
                    return res , ind
                
                # third if it is digit
                elif char.isdigit():
                    num = num * 10 + int(char)

                #if it is character
                else:
                    res+=char
                ind+=1
            return res , ind

        decoded , ind = helper(0)
        return decoded