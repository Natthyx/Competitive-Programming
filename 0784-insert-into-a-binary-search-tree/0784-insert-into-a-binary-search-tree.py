# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(node):
            if not node:
                return TreeNode(val)

            if node.val > val:
                node.left = search(node.left)
            elif node.val< val:
                node.right = search(node.right)

            return node
        

        
        return search(root)