# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/rotate-list/

from linkedList import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        # 两个指针，一个指针领先另外一个指针k次
        slow, fast = head, head
        counter = 0
        # 第一次，快指针向前移动k次，如果没到k次，就断了，则 k = k % 链表长度
        while counter < k and fast:
            fast = fast.next
            counter += 1
        if not fast and counter==k:
            return head
        elif not fast and counter<k:

            k = k % counter;
            counter=0
            fast = head
            if k == 0:
                return head
            while counter < k and fast:
                fast = fast.next
                counter += 1

        while fast.next:
            fast=fast.next
            slow=slow.next
        fast.next=head
        newHead = slow.next
        slow.next=None
        return newHead

l1 = ListNode()
l1.create_linklist([1, 2, 3, 4, 5])
k = 11
l1.printLL();
s = Solution()

for i in range(20):
    r = s.rotateRight(l1,i)
    r.printLL()
