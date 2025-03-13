class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(left, right, turn):
            # Base case: Only one element left
            if left == right:
                return nums[left] if turn == 1 else 0
            
            # If it's Player 1's turn, try to **maximize the score**
            if turn == 1:
                return max(
                    nums[left] + dfs(left + 1, right, 2),   # Pick left
                    nums[right] + dfs(left, right - 1, 2)   # Pick right
                )
            # If it's Player 2's turn, try to **minimize Player 1's score**
            else:
                return min(
                    dfs(left + 1, right, 1),   # Player 2 picks left
                    dfs(left, right - 1, 1)   # Player 2 picks right
                )
        
        # Total sum of nums
        total = sum(nums)
        
        # Score Player 1 can get
        player1_score = dfs(0, len(nums) - 1, 1)
        
        # Player 1 wins if their score is greater than or equal to Player 2's
        return player1_score >= (total - player1_score)
