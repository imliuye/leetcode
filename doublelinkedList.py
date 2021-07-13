class Node:
    def __init__(self, val, prev=None, next=None, random=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        self.random = random

    def append_linklist(self, arr: list):

        prev = self;
        for val in arr:
            curr = Node(val, prev, None)
            prev.next = curr
            prev = curr

    def printLL(self):
        head = self

        while (head):
            print(head.val, end=", ")
            head = head.next

        print("")

    def append(self, arr):
        curr = self
        for a in arr:
            node = Node(a)
            curr.next = node
            curr = node
