class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows , cols = len(matrix), len(matrix[0])
        ans = 0
        prefix = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                top = prefix[r-1][c] if r > 0 else 0
                left = prefix[r][c-1] if c > 0 else 0
                top_left = prefix[r-1][c-1] if min(r,c) > 0 else 0

                prefix[r][c] = matrix[r][c] + top + left - top_left

        for i in range(rows):
            for j in range(i,rows):
                count = defaultdict(int)
                count[0] = 1
                for c in range(cols):
                    cur_sum = prefix[j][c] - (prefix[i-1][c] if i > 0 else 0)
                    diff = cur_sum - target
                    ans += count[diff]
                    count[cur_sum] += 1

        return ans