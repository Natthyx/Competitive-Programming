# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = []
        right = []
        if not p and not q:
            return True

        def dfs(node, arr):
            if not node:
                arr.append(None)
                return
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)

            return arr

        if not p or not q:
            return False

        if not p and not q:
            return True

        k = dfs(p,left)
        l = dfs(q,right)

        return k == l