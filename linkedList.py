class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printLL(self):
        head = self

        while (head):
            print(head.val, end=", ")
            head = head.next

        print("")

    def append(self, arr):
        curr = self
        for a in arr:
            node = ListNode(a)
            curr.next = node
            curr = node

