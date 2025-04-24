# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        queue = deque([(0,0,root)])
        res = defaultdict(list)

        while queue:
            col,row,node = queue.popleft()
            nodes.append((col,row,node.val))

            if node.left:
                queue.append((col-1,row + 1, node.left))

            if node.right:
                queue.append((col + 1,row + 1, node.right,))
        
        nodes.sort()

        for col, row, val in nodes:
            res[col].append(val)
        
        return [res[v] for v in sorted(res)]


        