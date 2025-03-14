# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        count = 0
        def dfs(node):
            nonlocal count
            nonlocal ans
            if node:
                
                count+=1
                ans = max(ans,count)
                dfs(node.left)
                dfs(node.right)
                count-=1

            

        dfs(root)
        return ans