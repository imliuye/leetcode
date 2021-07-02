class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_Tree(self, arr: list):
        if not arr: return self
        value = arr.pop(0)
        head = self
        head.val = value
        layer = [head]
        while arr:
            for i in range(len(layer)):
                node = layer.pop(0)
                leftVal = arr.pop(0) if arr else None
                rightVal = arr.pop(0) if arr else None
                leftNode = TreeNode(leftVal) if leftVal else None;
                rightNode = TreeNode(rightVal) if rightVal else None;
                node.left = leftNode
                node.right = rightNode
                if leftNode:
                    layer.append(leftNode)
                if rightNode:
                    layer.append(rightNode)

        return head

    def depth(self):
        root = self
        q = [root]
        depth = 0
        levelQ = [root]
        while levelQ:
            depth += 1
            for i in len(levelQ):
                n = levelQ.pop(0)
                l = n.left;
                r = n.right;
                if l:
                    levelQ.append(l)
                if r:
                    levelQ.append(r)
        return depth

    def printTree(self, head):
        pass

# test
