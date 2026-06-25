class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        newNode = ListNode(homepage)
        newNode.prev = self.head
        newNode.next = self.tail
        self.head.next = newNode
        self.tail.prev = newNode

        self.curr = newNode

    def visit(self, url: str) -> None:
        if self.curr.next != self.tail:
            self.curr.next = self.tail
            self.tail.prev = self.curr

        next = self.tail
        prev = self.tail.prev

        newNode = ListNode(url)
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        
        self.curr = newNode

    def back(self, steps: int) -> str:
        for _ in range(steps):
            self.curr = self.curr.prev
            if self.curr == self.head:
                self.curr = self.curr.next
                return self.curr.val
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            self.curr = self.curr.next
            if self.curr == self.tail:
                self.curr = self.tail.prev
                return self.curr.val
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)