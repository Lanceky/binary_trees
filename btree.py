#binary tree in python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    #Travers preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    #traverse Inoder
    def traverseInOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traverseInOrder()
        if self.right:
            self.right.traverseInOrder()


    #Traverse Postorder
    def traversePostOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre order Traversal: ", end= "")
root.traversePreOrder()
print("\nIn Order Traversal: ", end= "")
root.traverseInOrder()
print("\n Post Order Traversal: ", end= '')
root.traversePostOrder()