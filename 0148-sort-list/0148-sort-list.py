# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMid(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        
        def merge(head):
            if not head or (not head.next):
                return head

            mid = findMid(head)

            right = merge(mid.next)
            mid.next = None
            left = merge(head)

            dummy = ListNode()
            curr = dummy

            while right and left:
                if left.val < right.val:
                    curr.next = ListNode(left.val)
                    left = left.next
                else:
                    curr.next = ListNode(right.val)
                    right = right.next

                curr = curr.next

            if right:
                curr.next = right
            if left:
                curr.next = left

            return dummy.next

        
        return merge(head)






        