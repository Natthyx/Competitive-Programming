# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        def bfs(queue,store):
            while queue:
                node = queue.popleft()
                store.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                elif not node.left:
                    store.append(None)
                elif not node.right:
                    store.append(None)

        p_store = []
        q_store = []

        if not p and (not q):
            return True
        if not p and q or (p and (not q)):
            return False
        p_queue = deque([p])
        q_queue = deque([q])
        bfs(p_queue,p_store)
        bfs(q_queue,q_store)

        return p_store == q_store
