# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy.next
        prev = dummy
        original = set()

        while curr:
            if curr.val in original:
                prev.next = curr.next
            else:
                original.add(curr.val)
                prev = curr
            
            curr = curr.next

        return dummy.next
        