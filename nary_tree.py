class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
    def __str__(self):
        return str(self.val)

    def create_nary_tree(self, arr):
        if not arr: return None
        root = Node(arr.pop(0))
        arr.pop(0)
        layer=[root]

        while arr:
            # 给孩子赋值
            print([node.val for node in layer])
            for i in range(len(layer)):
                node=layer.pop(0)
                childVal = []
                while arr and arr[0] != None:
                    childVal.append(arr.pop(0))
                childNodes = [Node(val) for val in childVal]
                node.children = childNodes
                layer.extend(childNodes)
                if arr:
                    arr.pop(0);





        return root

    def preorder(self, root: "Node"):
        if not root: return root
        # 用stack
        result=[]
        stack=[root]
        while stack:
            top = stack.pop(0)
            result.append(top.val)
            if top.children:
                stack = top.children + stack

        return result;
    def postorder(self, root: 'Node'):
        if not root:
            return root
        stack=[[root,False]]
        result=[]
        while stack:
            if stack[0][1] or not stack[0][0].children:
                result.append(stack.pop(0)[0].val)
                continue
            stack[0][1]=True
            stack = [[node, False] for node in stack[0][0].children] + stack

        return result;

    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        layer=[root]
        result=[]
        while layer:
            result.append([node.val for node in layer])
            for i in range(len(layer)):
                node=layer.pop(0)
                if node.children:
                    layer.extend(node.children)



        return result;


aa = Node()
val = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
ntree = aa.create_nary_tree(val)
pre = ntree.preorder(ntree)
post=ntree.postorder(ntree)
level=ntree.levelOrder(ntree)
print(pre)
print(post)
print(level)
