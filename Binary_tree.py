import pdb


class Node:
    def __init__(self,key):
        # pdb.set_trace()
        self.left=None
        self.right= None
        self.key= key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key)

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# print nodes at given levels
def printGivenLevel(root,level):
    if root is None:
        return
    if level==1 :
        print(root.key)
    elif level > 1:
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right, level-1)


def insert(node,key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left= insert(node.left,key)
    else:
        node.right= insert(node.right,key)
    return node


def minvalue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deletenode(node,key):

    if node is None:
        return node
    if key < node.key:
        node.left = deletenode(node.left,key)
    elif key > node.key:
        node.right = deletenode(node.right,key)
    else:
        # pdb.set_trace()
        if node.left is None:
            tmp = node.right
            node = None
            return tmp
        elif node.right is None:
            tmp = node.left
            node = None
            return tmp
        temp = minvalue(node.right)
        node.key = temp.key
        node.right = deletenode(node.right, temp.key)

    return node

def balance(keys):
    if not keys:
        return None
    else:
        mid=len(keys)//2
        node = Node(keys[mid])
        node.left= balance(keys[:mid])
        node.right= balance(keys[mid+1:])
        return node

n = Node(20)
n.left = Node(10)
n.left.left = Node(5)
# n.right=Node(12)
# n.right.right=Node(6)
# n.right.right.right=Node(100)

insert(n, 50)
insert(n, 12)

insert(n, 100)
print(balance([1,2,3,4,5,6,7,8,9]))
print()
deletenode(n, 10)
print()
# print(height(n))
# for i in range(height(n)+1):
#     printGivenLevel(n,i)
inorder(n)

print()
preorder(n)
print()
postorder(n)