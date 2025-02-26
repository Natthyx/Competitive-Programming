# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        res = ListNode()
        ans = res
        while l1:
            num1+= str(l1.val)
            l1 = l1.next

        while l2:
            num2+= str(l2.val)
            l2 = l2.next

        sm = int(num1[::-1])+int(num2[::-1])
        sm = list(map(int,str(sm)[::-1]))
        i = 0
        while ans:
            if i >= len(sm):
                break
            ans.next = ListNode(sm[i])
            ans = ans.next
            i += 1

        return res.next
        


