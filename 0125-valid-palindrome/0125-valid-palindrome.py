class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        t = s[::-1]
        if s.lower() == t.lower():
            return True
    
        