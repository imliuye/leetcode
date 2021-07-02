# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/binary-tree-tilt/
from treeNode import TreeNode;
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            root.sum = root.val
            return root.val
        def calcSum(node):
            if not node:
                return 0
            if not node.left and not node.right:
                node.sum = node.val
                return node.val
            try:
                return node.sum
            except AttributeError:
                node.sum = 0

            node.sum = calcSum(node.left) + calcSum(node.right) + node.val
            return node.sum
        calcSum(root)

        sumOfTilt = 0

        # 遍历
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0);
                left,right=0,0
                if node.left:
                    queue.append(node.left)
                    left = node.left.sum
                if node.right:
                    queue.append(node.right)
                    right = node.right.sum
                sumOfTilt += abs(left-right)
        return sumOfTilt

s = Solution()
# root = TreeNode(4,
#                 left=TreeNode(2, left=TreeNode(3),right=TreeNode(5)),
#                 right=TreeNode(9,right=TreeNode(7))
#                 );
root = TreeNode(4)
root.create_Tree([4,2,9,3,5,None,7])
r = s.findTilt(root)
print(r)
root = TreeNode(1)
root.create_Tree([21,7,14,1,1,2,2,3,3])
r = s.findTilt(root)
print(r)
