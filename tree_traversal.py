class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if root :
        inorder(root.left)
        print root.val
        inorder(root.right)
    else:
        return

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
    else:
        return

def preorder(root):
    if root:
        print (root.val)
        preorder(root.left)
        preorder(root.right)
    else:
        return

#used to print in non-increasing order for a BST
def rev_inorder(root):
    if root:
        rev_inorder(root.right)
        print(root.val)
        rev_inorder(root.left)
    else:
        return

#main code
node1 = Node(3)
node2 = Node(1)
node3 = Node(7)
node4 = Node(2)
node5 = Node(4)
node7 = Node(9)
node1.left = node2
node1.right = node3
node2.right = node4
node3.left = node5
node3.right = node7

inorder(node1)
preorder(node1)
postorder(node1)
rev_inorder(node1)

#print node3.right
#print node1.right
