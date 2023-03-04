# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while True:
                    if slow == head:
                        return head
                    else:
                        head = head.next
                        slow = slow.next
                        if slow == head:
                            return head
        # if not fast or not fast.next:
        return None

        

