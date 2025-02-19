# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        end = head

        while end != None:
            n+=1
            end = end.next
        left = (n//2)+1

        count = 0
        curr = head

        while curr != None:
            count+=1
            if count == left:
                return curr
            
            curr = curr.next

        

       
        




        