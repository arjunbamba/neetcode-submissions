class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        for _ in range(index):
            curr = curr.next
            if not curr:
                return -1
        if curr == self.right:
            return -1
            
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        next = self.left.next
        prev = self.left

        newNode.next = next
        newNode.prev = prev
        next.prev = newNode
        prev.next = newNode


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        next = self.right
        prev = self.right.prev

        newNode.next = next
        newNode.prev = prev
        next.prev = newNode
        prev.next = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:

        curr = self.left.next
        for _ in range(index):
            curr = curr.next
            if not curr:
                return
        if curr == self.right:
            self.addAtTail(val)
            return
        
        newNode = ListNode(val)
        next = curr
        prev = curr.prev

        newNode.next = next
        newNode.prev = prev
        next.prev = newNode
        prev.next = newNode
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        for _ in range(index):
            curr = curr.next
            if not curr: # index > length
                return
        if curr == self.right:
            return
        
        next = curr.next
        prev = curr.prev
        prev.next = next
        next.prev = prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)