class ListNode:
    def __init__(self,key, val,prev=None,nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.cache = {}
        self.length = 0
        self.capacity = capacity
        
    def ptrmoving(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            if node != self.head and node != self.tail:
                self.ptrmoving(node)
            elif node == self.tail and node != self.head:
                self.tail = self.tail.prev

                node.next = self.head
                self.head.prev = node

                self.head = self.head.prev

                node.prev = None
                self.tail.next = None

            return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return 
        if not self.head and not self.tail:
            newnode = ListNode(key, value)

            self.head = newnode
            self.tail = newnode

            self.cache[key] = newnode
            self.length+=1
            return


        if self.length < self.capacity:
            newnode = ListNode(key, value)
            newnode.next = self.head

            self.head.prev = newnode
            self.head = self.head.prev

            self.cache[key] = newnode
            self.length+=1

        else:
            newnode = ListNode(key, value)
            if self.head == self.tail:
                del self.cache[self.head.key]
                self.head = newnode
                self.tail = newnode
            else:
                temp = self.tail

                self.tail = self.tail.prev
              
                temp.prev = None
                self.tail.next = None

                newnode.next = self.head
                self.head.prev = newnode
                self.head = self.head.prev
                del self.cache[temp.key]

            self.cache[key] = newnode


            





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)