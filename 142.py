# https://leetcode.com/problems/linked-list-cycle-ii/

# 第一次快慢指针相交的位置，那么交叉点，应该在这个位置之前。我们叫做 firstMeetNode,
# 第二次，从head，走到firstMeetNode 的长度为fm
# (这一步不用执行)第三次，从firstMeetNode出发，第二次走到FistMeetNode停下，圈圈的长度为cc
# sm(second meet) sm = fm + c；fm==cc
# 圈圈的长度为：c=sm-fm
# 最后，一个从head走，一个从firstMeetNode走，相等的点，就是焦点


from linkedList import ListNode
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head,head
        firstMeetNode = None
        fm = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            fm += 1
            if not fast:
                return None

            if slow == fast:
                firstMeetNode = slow
                break


        first = head
        second = firstMeetNode

        while first !=second:
            first = first.next
            second =second.next

        return first


head = ListNode(3)
n2 =ListNode(2)
n3 =ListNode(0)
n4 =ListNode(-4)
head.next = n2;
n2.next=n3
n3.next=n4
n4.next=n2

# head.printLL();


s = Solution()

r = s.detectCycle(head)
print(r.val)

