# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        n1 = ListNode(-1)
        head = n1
        while l1 and l2:
            if l1.val < l2.val:
                newNode = ListNode(l1.val)
                n1.next = newNode
                n1 = n1.next
                l1 = l1.next
            elif l2.val < l1.val:
                newNode = ListNode(l2.val)
                n1.next = newNode
                n1 = n1.next
                l2 = l2.next
            else:
                newNodeL1 = ListNode(l1.val)
                newNodeL2 = ListNode(l2.val)
                n1.next = newNodeL1
                n1 = n1.next
                n1.next = newNodeL2
                n1 = n1.next
                l1 = l1.next
                l2 = l2.next
        
        while l1:
            n1.next = ListNode(l1.val)
            n1 = n1.next
            l1 = l1.next
        
        while l2:
            n1.next = ListNode(l2.val)
            n1 = n1.next
            l2 = l2.next
        
        return head.next
        
            
        




