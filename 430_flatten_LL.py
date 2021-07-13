# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

from doublelinkedList import Node


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        stack = [head]
        tail = None;
        while stack:
            node = stack.pop(-1)
            if tail:
                tail.next = node
                node.prev = tail
                tail = None
            while node:
                if node and node.child:
                    if node.next:
                        stack.append(node.next)
                    node.child.prev = node
                    node.next = node.child
                    node.child = None
                elif not node.next:
                    tail = node

                node = node.next
        return head

head = Node(1)
head.append_linklist([2, 3, 4, 5, 6])
head2 = head.next.next.child = Node(7)
head2.append_linklist([8, 9, 10])
head3 = head2.next.child = Node(11)
head3.append_linklist([12])
head.printLL();
head2.printLL();
head3.printLL();

s = Solution()

r = s.flatten(head)
r.printLL()
