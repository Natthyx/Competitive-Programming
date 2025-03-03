# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ''
        b = ''

        while l1:
            a+=str(l1.val)
            l1 = l1.next

        while l2:
            b+=str(l2.val)
            l2 = l2.next

        sm = int(a)+int(b)
        sm = list(map(int,str(sm)))

        dummy = ListNode()
        ans = dummy
        i = 0
        while ans:
            if i >= len(sm):
                break
            ans.next = ListNode(sm[i])
            ans = ans.next
            i += 1


        return dummy.next


        


