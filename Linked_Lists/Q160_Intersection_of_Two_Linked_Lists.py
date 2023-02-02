# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. Find the lengths of the two given lists.
# 2. Make the list equal by removing some elements.
# 3. Step 2 is done by updating the head pointer.
# 4. Traverse the list and check for the common node.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = lenB = 0
        dummy_A = headA
        dummy_B = headB
        while dummy_A or dummy_B:
            if dummy_A:
                dummy_A = dummy_A.next 
                lenA += 1
            if dummy_B:
                dummy_B = dummy_B.next
                lenB += 1 
        diff = abs(lenB-lenA)
        if lenB > lenA:
            for i in range(diff):
                headB = headB.next
        elif lenA > lenB:
            for i in range(diff):
                headA = headA.next
        
        while (headA != headB) and (headA.next != None):
            headA = headA.next
            headB = headB.next
        return headA if headA == headB else None
