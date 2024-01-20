class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number=0
        for alpha in columnTitle:
            number=number*26 + (ord(alpha)-64)
        return number
        