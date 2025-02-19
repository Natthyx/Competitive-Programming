# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        dummy1.next = list1
        dummy2.next = list2
        
        left = list1
        right = list2
        prevleft, prevright = dummy1, dummy2

        while left and right:
            currleft = left
            curright = right

            if left.val <= right.val:
                left = left.next
                
            else:
                right = right.next
                prevleft.next = curright
                curright.next = left
            prevleft = prevleft.next
                
       
        if right:
            prevleft.next = right
        
        return dummy1.next


            



            



            
            



