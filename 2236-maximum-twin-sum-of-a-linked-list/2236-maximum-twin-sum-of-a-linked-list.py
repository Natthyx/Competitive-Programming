# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        l , r = 0, len(arr)-1
        ans = 0
        while l < r:
            ans = max(ans, arr[l]+arr[r])
            l+=1
            r-=1

        return ans