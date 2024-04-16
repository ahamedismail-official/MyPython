class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def bst(root,val):
    if root is None:
        return node(val)
    elif root.data > val:
        root.left=bst(root.left,val)
    elif root.data < val:
        root.right=bst(root.right,val)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data)
        inorder(root.left)
        inorder(root.right)
def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.data)
root=node(40)
n=int(input())
for i in range(n):
    ele=int(input())
    bst(root,ele)
inorder(root)