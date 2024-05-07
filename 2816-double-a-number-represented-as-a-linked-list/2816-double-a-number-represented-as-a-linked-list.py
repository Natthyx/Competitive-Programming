import sys
sys.set_int_max_str_digits(10000000)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def intToList(num):
            return [int(digit) for digit in str(num)]
        
        def list_to_linked_list(num):
            if not num:
                return None
            head = ListNode(num[0])
            current = head
            for value in num[1:]:
                current.next = ListNode(value)
                current = current.next
            return head
        
        lis = []
        current = head
        
        while current:
            lis.append(current.val)
            current = current.next
        
        
        num_str = ''.join(map(str, lis))
        
        doubleEle = int(num_str) * 2
        
        lst = intToList(doubleEle)
        
        return list_to_linked_list(lst)
        
        
        
        
        
        