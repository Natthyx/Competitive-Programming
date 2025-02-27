class ListNode:
    def __init__(self, val, prev= None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.home = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.home.next = ListNode(url, self.home)
        self.home = self.home.next
        

    def back(self, steps: int) -> str:
        while self.home.prev and steps > 0:
            self.home = self.home.prev
            steps -= 1

        return self.home.val
        

    def forward(self, steps: int) -> str:
        while self.home.next and steps > 0:
            self.home = self.home.next
            steps-=1
        return self.home.val
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)