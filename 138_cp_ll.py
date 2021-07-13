# https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from randomLinkedList import Node


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        counter = 0
        curr = head
        while curr:
            curr.index = counter
            counter += 1
            curr = curr.next

        index_node = dict()
        new_head = Node(head.val)
        new_node = new_head
        old_node = head
        index_node[0] = new_node
        counter = 0
        while old_node:
            index_node[counter] = new_node
            next_new_node = Node(old_node.next.val) if old_node.next else None
            new_node.next = next_new_node
            old_node = old_node.next
            new_node = next_new_node
            counter += 1

        new_node = new_head
        old_node = head

        while old_node:
            if old_node.random:
                new_node.random = index_node[old_node.random.index]
            old_node = old_node.next
            new_node = new_node.next
        return new_head


head = Node(1)
head.append_linklist([2, 3, 4, 5, 6])
head.printLL()
print('---')
s = Solution(
)
result = s.copyRandomList(head)
result.printLL()
