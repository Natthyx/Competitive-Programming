class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter = Counter(s)

        for ch in s:
            count = 0
            if not stack:
                stack.append([ch,1])
            else:
                if stack[-1][0] == ch:
                    stack[-1][1] += 1
                    if stack[-1][-1] and stack[-1][-1] >= k:
                        stack.pop()
                else:
                    stack.append([ch,1])
        
        ans = ''
        for ch,count in stack:
            ans+= (ch*count)

        return ans