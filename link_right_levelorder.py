class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.nextRight = None

def height(root):
    if root is None:
        return 0
    else :
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def samelevel(root, i, nodes):
    if root is None:
        return []
    elif i==1:
        #return [root.val]
        return[root]
    else:
        return samelevel(root.left, i-1, nodes)+samelevel(root.right, i-1, nodes)

def levelorder(root):
    h = height(root)
    for i in range(1,h+1):
        nodes = []
        nodes = samelevel(root,i, nodes)
        #print nodes
        for j in range(len(nodes)-1):
            #print nodes[j].val
            nodes[j].nextRight = nodes[j+1]
            #print nodes[j].nextRight.val
        #print nodes[len(nodes)-1].val
        nodes[len(nodes)-1].nextRight = None
        #print nodes[len(nodes)-1].nextRight
        

'''def nextright(root):
    h = height(root)
    for i in range(1,h+1):
        nodes = []
        nodes = samelevel(root,i, nodes)
        #print nodes
        for j in range(len(nodes)-1):
            if nodes[j].nextRight is not None :
                print nodes[j].nextRight.val
            else:
                print "None"
'''
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

levelorder(node1)
#nextright(node1)
print (node1.nextRight)
print (node2.nextRight.val)
print (node3.nextRight)
print (node4.nextRight.val)
print (node5.nextRight.val)
print node7.nextRight
