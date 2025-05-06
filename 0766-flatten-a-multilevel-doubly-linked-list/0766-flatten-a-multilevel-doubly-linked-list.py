"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''

        - traverse on the linkedlist
        - when we find a node that have child, we will call a recursion to do the same
        traverse
        - 

        '''
        dummy = Node(0,None,None,None)
        tail = dummy
        

        def helper(node):
            nonlocal tail
            if not node:
                return
            
            while node:
                new_node = Node(node.val,tail,None,None)
                tail.next = new_node
                tail = new_node

                next_node = node.next

                if node.child:
                    helper(node.child)
                    node.child = None
                
                node = next_node
        
        helper(head)
        if dummy.next:
            dummy.next.prev = None
        return dummy.next



        