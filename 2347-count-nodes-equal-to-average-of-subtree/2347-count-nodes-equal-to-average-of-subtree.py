# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return (0,0)

            Rtotal , Rnum = dfs(node.right)
            Ltotal , Lnum = dfs(node.left)
            
            total = Rtotal + Ltotal + node.val
            num = Rnum + Lnum + 1
            
            if total // num == node.val:
                count +=1
                
            return (total,num)

        dfs(root)
        return count