# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        if head == None:
            return False
        while slow.next and fast.next:
            if fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
