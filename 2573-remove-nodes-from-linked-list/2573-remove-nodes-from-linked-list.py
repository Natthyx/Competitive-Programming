# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        while head:
            while stack and head.val > stack[-1]:
                stack.pop()
            stack.append(head.val)
            head = head.next
        
        dummy = ListNode()
        tail = dummy

        for i in stack:
            tail.next = ListNode(i)
            tail = tail.next

        return dummy.next
