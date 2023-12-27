class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        reverse=num_str[::-1]
        if reverse == num_str:
            return True

        