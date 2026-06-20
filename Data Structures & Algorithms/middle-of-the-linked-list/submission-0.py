# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        if length % 2:
            length = (length // 2)
        else:
            length /= 2
        
        while length:
            head = head.next
            length -= 1
        
        return head