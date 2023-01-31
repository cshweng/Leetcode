# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy_node = ListNode()
        add = ListNode()
        while l1 or l2:
            x = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add.val
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if x <10:
                dummy_node.next = ListNode(x)
                add = ListNode()
            else:
                dummy_node.next = ListNode(x - 10)
                add = ListNode(1)
            dummy_node = dummy_node.next
        if add.val == 1:
            dummy_node.next = add
        return node.next
