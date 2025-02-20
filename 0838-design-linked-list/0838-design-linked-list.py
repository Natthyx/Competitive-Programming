class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
  
    def get(self, index: int) -> int:
        curr = self.dummy.next
        currIndex = 0
        while curr:
            if currIndex == index:
                return curr.val
            curr = curr.next
            currIndex+=1
        
        return -1

        
    def addAtHead(self, val: int) -> None:
        first = ListNode(val)
        first.next = self.dummy.next
        self.dummy.next = first

    def addAtTail(self, val: int) -> None:
        last = ListNode(val)
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = last

    def addAtIndex(self, index: int, val: int) -> None:
        currIndex = 0
        curr = self.dummy.next
        prev = self.dummy
        newNode = ListNode(val)
        while prev:
            if currIndex == index:
                newNode.next = curr
                prev.next = newNode
                break
            prev = curr
            if curr:
                curr = curr.next
            currIndex+=1
        

    def deleteAtIndex(self, index: int) -> None:
       
        curr = self.dummy.next
        prev = self.dummy
        count = 0
        while curr:
            if count == index:
                prev.next = curr.next
                break
            
            prev = curr
            curr = curr.next
            count += 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)