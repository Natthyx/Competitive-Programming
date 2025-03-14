# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def searching(node):
            if not node:
                return None
        
            if node.val > val:
                node.left = searching(node.left)
                return node.left
            elif node.val < val:
                node.right = searching(node.right)
                return node.right
                
            else:
                return node

        return searching(root)
