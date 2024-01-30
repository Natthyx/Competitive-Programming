# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2
        carry = 0
        ans = None
        head = None
        
        while num1 and num2:
            add = num1.val + num2.val + carry
            carry = add//10
            add %= 10
            
            temp = ListNode(add)
            temp.next = None
            
            if ans:
                ans.next = temp
                ans = ans.next
            else:
                ans = temp
                head = ans
            
            num1 = num1.next
            num2 = num2.next
        
        while num1:
            add = num1.val + carry
            carry = add//10
            add %= 10
            temp = ListNode(add)
            temp.next = None

            if ans:
                ans.next = temp
                ans = ans.next
            else:
                ans = temp
                head = ans

            num1 = num1.next
        
        while num2:
            add = num2.val + carry
            carry = add//10
            add %= 10
            temp = ListNode(add)
            temp.next = None

            if ans:
                ans.next = temp
                ans = ans.next
            else:
                ans = temp
                head = ans
        
            num2 = num2.next
            
        if carry > 0:
            temp = ListNode(carry)
            temp.next = None

            if ans:
                ans.next = temp
                ans = ans.next
            else:
                ans = temp
                head = ans
        
        return head