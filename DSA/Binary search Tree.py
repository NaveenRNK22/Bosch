class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

def insert(root,key):
    if root is None:
        return Node(key)
    elif root.key == key:
        return root
    elif root.key > key:
        root.right = insert(root.right,key)
    else:
        root.left = insert(root.left,key)
    return root

def search(root,key):
    if root.key == key or root is None:
        return root
    elif root.key > key:
        return search(root.right,key)
    else:
        return search(root.left,key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key," ", end='')
        inorder(root.right)
    
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key," ", end='')

def preorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.key," ", end='')


r = Node(50)

r=insert(r,10)
r=insert(r,40)
r=insert(r,70)
r=insert(r,90)
r=insert(r,20)
r=insert(r,80)
r=insert(r,30)
r=insert(r,60)

inorder(r)
print("")
postorder(r)
print("")
preorder(r)