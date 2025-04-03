# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dp = {}
        ans = float("-inf")

        def dfs(node):
            nonlocal ans
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)

            left,right = 0 , 0
            if node.left:
                left = max(left,dp[node.left])
            if node.right:
                right = max(right,dp[node.right])

            ans = max(ans, (left + right + node.val))
            dp[node]=(node.val+(max(left,right)))
            ans = max(ans,dp[node])

        dfs(root)

        return ans
