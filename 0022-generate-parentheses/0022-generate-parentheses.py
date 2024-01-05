class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate("", n, n, result)
        return result

    def generate(self, current, left, right, result):
        if left == 0 and right == 0:
            result.append(current)
            return

        if left > 0:
            self.generate(current + "(", left - 1, right, result)
        if right > left:
            self.generate(current + ")", left, right - 1, result)
        