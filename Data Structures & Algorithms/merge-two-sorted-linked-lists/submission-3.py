# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        dummy = n1 = ListNode(-1)

        while l1 and l2:
            if l1.val < l2.val:
                n1.next = l1
                l1 = l1.next
            else:
                n1.next = l2
                l2 = l2.next
            
            n1 = n1.next
        
        n1.next = l1 or l2

        return dummy.next