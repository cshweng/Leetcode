# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = head
        if dummy_node.next == None:
             return None
        x=0
        while dummy_node:
            x+=1
            dummy_node = dummy_node.next
        dummy_node = head
        if x==n:
            return head.next
        else:
            for i in range(x-n-1):
                dummy_node = dummy_node.next
            dummy_node.next = dummy_node.next.next
            return head


