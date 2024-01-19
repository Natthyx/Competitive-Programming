class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows , cols = len(matrix) , len(matrix[0])
        
        for row in range(1,rows):
            for col in range(cols):
                matrix[row][col] += min(
                matrix[row-1][col-1] if col>0 else float("inf"),
                matrix[row-1][col],
                matrix[row-1][col+1] if col < cols-1 else float("inf"))
                
        return min(matrix[-1])
        