# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        stack = deque([root])
        # print(root.left,root.right,root.val)
        mx = 0

        while stack:
            ln = len(stack)

            for _ in range(ln):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                
                # print(stack)
                
                stack2 = deque([node])
                while stack2:
                    ln = len(stack2)

                    for _ in range(ln):
                        node2 = stack2.popleft()
                        if node2.left:
                            stack2.append(node2.left) 
                        if node2.right:
                            stack2.append(node2.right)
                        # print(stack2)
                        # print(node.val,node2.val)
                        mx = max(mx, abs(node.val - node2.val))
        # print(mx)
        return mx

        