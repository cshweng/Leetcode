class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def append(self, val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    def showLinkedList(self):
        dummy_node = self.head
        while dummy_node:
            print(f"{dummy_node.val}->",end="")
            dummy_node = dummy_node.next
        print("None")
