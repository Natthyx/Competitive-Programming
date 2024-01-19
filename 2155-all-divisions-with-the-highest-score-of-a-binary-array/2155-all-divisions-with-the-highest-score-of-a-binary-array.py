class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum_zeros = [0] * (n + 1)
        prefix_sum_ones = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sum_zeros[i] = prefix_sum_zeros[i - 1] + (nums[i - 1] == 0)
            prefix_sum_ones[i] = prefix_sum_ones[i - 1] + (nums[i - 1] == 1)

        max_score = -1
        result = []

        for i in range(n + 1):
            left_zeros = prefix_sum_zeros[i]
            right_ones = prefix_sum_ones[n] - prefix_sum_ones[i]

            score = left_zeros + right_ones

            if score > max_score:
                max_score = score
                result = [i]

            elif score == max_score:
                result.append(i)

        return result

            
            
                
                