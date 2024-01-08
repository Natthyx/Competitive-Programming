class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1

        ans = [list(triplet) for triplet in result]
        return ans
