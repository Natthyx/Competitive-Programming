# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                levels[count].append(None)
                return
            else:
                levels[count].append(node.val)
            
            
            count+=1
            dfs(node.left)
            dfs(node.right)
            
            count-=1

        
        dfs(root)

        for key in levels:
            if levels[key] != levels[key][::-1]:
                return False

        

        return True