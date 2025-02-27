# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        ans = 0
        while prev:
            ans = max(ans, head.val+prev.val)
            prev = prev.next
            head = head.next

        return ans







        # arr = []

        # while head:
        #     arr.append(head.val)
        #     head = head.next

        # l , r = 0, len(arr)-1
        # ans = 0
        # while l < r:
        #     ans = max(ans, arr[l]+arr[r])
        #     l+=1
        #     r-=1

        # return ans