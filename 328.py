# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedList import ListNode;


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:

            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next

        odd.next= evenHead
        return  head

head = ListNode(2)
head.append([1,3,5,6,4,7])
head.printLL();

s = Solution()

r = s.oddEvenList(head)
r.printLL()
