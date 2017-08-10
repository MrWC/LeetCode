'''
we have a binary tree, print out the in order walk of the tree as a doubly linked list, and do everything in memory
       2
   /      \
  1         8
/ \        /  \
10 11      3   5

10 => 1 => 11 => 2 => 3 => 8 => 5 => 10
'''


class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.next = None

linkedList = []
def inOrderWalk(root,linkedList):
    if root:
        if root.left:
            inOrderWalk(root.left,linkedList)
        linkedList.append(root.value)
        if root.right:
            inOrderWalk(root.right,linkedList)
     
def createLink(root,lastNode):
    if root:
        if root.left:
            lastNode = createLink(root.left,lastNode)
            
        if lastNode:
            lastNode.next = root
            lastNode = root
        else:
            lastNode = root
            
        if root.right:
            lastNode = createLink(root.right,lastNode)
        # print(lastNode.value)
        return lastNode

root = Node(2)
root.right = Node(8)
root.left = Node(1)
root.left.left = Node(10)
root.left.right = Node(11)
root.right.left = Node(3)
root.right.right = Node(5)
# root.left.right.right = Node(15)
inOrderWalk(root,linkedList)
print(linkedList)

lastNode = createLink(root,None)
lastNode = root.left.left
while lastNode:
    print(lastNode.value, end=", ")
    lastNode = lastNode.next
