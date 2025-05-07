# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            while lst:
                heapq.heappush(heap,lst.val)
                lst = lst.next
        
        heap.sort()
        dummy = ListNode(0)
        tail = dummy

        for i in range(len(heap)):
            tail.next = ListNode(heap[i])
            tail = tail.next
        
        return dummy.next