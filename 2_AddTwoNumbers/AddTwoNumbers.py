# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = (l1.val + l2.val) % 10
        addOne = int( (l1.val + l2.val) / 10)
        head =  ListNode(first)
        current = head
        nextNode = None
        print ("first ",first)
        print ("addOne", addOne)
        l1 = l1.next
        l2 = l2.next
        while l1 or l2 or addOne == 1:
            val1 = 0 if l1 == None else l1.val
            val2 = 0 if l2 == None else l2.val
            first =  (val1+val2+addOne) % 10
            
            print("val1 , val2, addOne",val1,val2,first)
            newNode = ListNode( (val1+val2+addOne) % 10)
            addOne = int ( (val1+val2+addOne) / 10 )
            current.next = newNode
            current = newNode
            l1 = None if l1==None else l1.next
            l2 = None if l2==None else l2.next
            
        return head
