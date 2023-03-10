class BinaryTreeNode():
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(12)
node7 = BinaryTreeNode(6)

node1.leftchild = node2
node1.rightchild = node3
node2.leftchild = node4
node2.rightchild = node5
node3.rightchild = node6
node3.leftchild = node7
print("Root node is:",node1.data)
print("right child of 2nd node is:",node5.data)
print("left child of 3rd node is:",node7.data)
