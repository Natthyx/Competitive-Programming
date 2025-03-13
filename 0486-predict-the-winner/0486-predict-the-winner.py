class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        def helper(left, right, turn):
            if left > right:
                return 0
            
            if turn:
                return max(nums[left] + helper(left + 1, right, False),
                           nums[right] + helper(left, right - 1, False))
            else:
                return min(helper(left + 1, right, True),
                           helper(left, right - 1, True))

        player1 = helper(0, len(nums) - 1, True)
        return player1 >= (total - player1)
