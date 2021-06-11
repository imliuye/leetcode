
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __init__(self, arr:list):
        if not arr: return None
        head = TreeNode(arr.pop(0))
        q = [head]
        while arr :
            while q:
                node = q.pop(0)
                leftVal = arr.pop(0)
                rightVal = arr.pop(0)
                leftNode = TreeNode(leftVal) if leftVal else None;
                rightNode = TreeNode(rightVal) if rightVal else None;
                if node:
                    node.left = leftNode
                    node.right = rightNode
                q.extend([leftNode,rightNode])

        return head

    def depth(self):
        root = self
        q = [root]
        depth = 0
        levelQ = [root]
        while levelQ:
            depth +=1
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
