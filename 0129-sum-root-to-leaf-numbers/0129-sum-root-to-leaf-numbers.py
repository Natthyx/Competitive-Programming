# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        stack = []
        
        def dfs(node,s):
            if not node:
                return

            s += str(node.val)
            
            if not node.left and not node.right:
                ans.append(int(s))
                return
            dfs(node.left,s)
            dfs(node.right,s)
            

        
        dfs(root,"")

        return sum(ans)

            



