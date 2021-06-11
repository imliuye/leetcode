#https://leetcode.com/problems/middle-of-the-linked-list/
from linkedList import ListNode
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow,fast = head,head
        while fast:
            fast = fast.next
            if not fast:
                return slow
            fast = fast.next;
            slow = slow.next

            if not fast:
                return slow

        return slow

head = ListNode(1)
head.append([2,3])
head.printLL();


s = Solution()

r = s.middleNode(head)
print(r.val)
