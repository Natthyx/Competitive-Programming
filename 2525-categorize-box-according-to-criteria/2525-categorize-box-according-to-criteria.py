class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = width * height * length
        if volume >= 10 ** 9 or length >= 10 **4 or height >= 10 **4 or width >= 10 **4:
            if mass>=100:
                return "Both"
            return "Bulky"
        if mass >= 100:
            return "Heavy"
        else:
            return "Neither"
        