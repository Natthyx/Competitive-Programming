# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        mx = 0

        while queue:
            ln = len(queue)
            for _ in range(ln):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                queue2 = deque([node])
                
                while queue2:
                    ln = len(queue2)
                    for _ in range(ln):
                        node2 = queue2.popleft()
                        if node2.left:
                            queue2.append(node2.left) 
                        if node2.right:
                            queue2.append(node2.right)
                        mx = max(mx, abs(node.val - node2.val))
        return mx      