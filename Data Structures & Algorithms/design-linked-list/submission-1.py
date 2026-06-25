class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        if not curr:
            return -1

        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, None, None)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode
        if not self.tail:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val, None, None)
        newNode.prev = self.tail
        if self.tail:
            self.tail.next = newNode
        self.tail = newNode
        if not self.head:
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        for _ in range(index):
            if not curr:
                break
            curr = curr.next

        newNode = ListNode(val, None, None)

        if not curr: 
            # last
            if self.tail:
                self.tail.next = newNode
                newNode.prev = self.tail
            self.tail = newNode
            return

        prev = curr.prev

        if not prev: # first
            newNode.next = curr
            curr.prev = newNode
            self.head = newNode
            return
        
        prev.next = newNode
        newNode.prev = prev

        newNode.next = curr
        curr.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for _ in range(index):
            if not curr:
                break
            curr = curr.next
        
        if not curr:
            return
        
        prev = curr.prev
        next = curr.next

        if not prev and not next:
            self.head = self.tail = None
        elif not prev:
            next.prev = None
            self.head = next
        elif not next:
            prev.next = None
            self.tail = prev
        else:
            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)