# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head , head
        curr = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        tail = slow
        
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp
        
        while prev and head:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next

        return True
        
