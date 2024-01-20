class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = ''
        for row in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(row, len(s), increment):
                result += s[i]
                middleCharacterIndex = i + increment - 2 * row
                if row != 0 and row != numRows - 1 and middleCharacterIndex < len(s):
                    result += s[middleCharacterIndex]
        
        return result