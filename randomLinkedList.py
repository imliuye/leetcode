class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def append_linklist(self, arr: list):

        self.val = arr.pop(0)
        currNode = self;
        for val in arr:
            nextNodde = Node(val)
            currNode.next = nextNodde;
            currNode = nextNodde

    def printLL(self):
        head = self

        while (head):
            print("[",head.val,head.random.val if head.random else "-", ']', end=", ")
            head = head.next

        print("")

    def append(self, arr):
        curr = self
        for a in arr:
            node = Node(a)
            curr.next = node
            curr = node
