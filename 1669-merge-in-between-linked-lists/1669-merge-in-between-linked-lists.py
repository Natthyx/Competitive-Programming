# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        lst1 = ListNode()
        lst2 = ListNode()
        
        dummy1 = lst1
        dummy2 = lst2
        
        cur = list1
        
        i=0
        while cur:
            if i < a:
                dummy1.next = cur
                dummy1 = dummy1.next
            if i == a:
                dummy1.next = None
            if i >= a and i<=b:
                cur = cur.next
                i+=1
                continue
            if i > b:
                dummy2.next = cur
                dummy2 = dummy2.next
            cur = cur.next
            i+=1
        dummy1.next = list2
        
        cur = lst1
        while cur and cur.next:
            cur= cur.next
        cur.next =lst2.next
        return lst1.next