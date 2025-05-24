class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(" ")
        for i in range(len(lst)-1,-1,-1):
            if lst[i] == "":
                continue
            else:
                return len(lst[i])
        
        