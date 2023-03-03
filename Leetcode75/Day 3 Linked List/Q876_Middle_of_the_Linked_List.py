# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        if head.next == None:
            return head
        elif head.next.next==None:
            return head.next
        while head:
            head = head.next.next
            dummy = dummy.next
            if head.next == None:
                return dummy
            elif head.next.next == None:
                return dummy.next

