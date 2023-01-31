# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = head
        if dummy_node == None:
            return head
        while dummy_node.next!=None:
            while dummy_node.val == dummy_node.next.val:
                if dummy_node.next.next!=None:
                    dummy_node.next = dummy_node.next.next
                else:
                    dummy_node.next = None
                    return head
            dummy_node = dummy_node.next
        return head
