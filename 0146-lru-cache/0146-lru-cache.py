class Node:
    def __init__(self, val , key, next=None , prev=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map the key -> pointer of the node

        self.left = Node(0,0)
        self.right = Node(0,0)

        #make left and right connected
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        nxt = node.next
        prev = node.prev

        prev.next = nxt
        nxt.prev = prev

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        prev.next = node
        node.next = nxt
        nxt.prev = node
        

    def get(self, key: int) -> int:
        # check if key is in cache
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # check if key in cache
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(value,key)
        self.insert(self.cache[key])

        # check if the capacity is full
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)