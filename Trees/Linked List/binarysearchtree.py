class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        pass

    def insert(self,root,data):
        if root is None:
            root.val = data
            return root
        if root.val == data:
            return 0
        elif root.val > data:
            root.left =  self.insert(root.left,data)
        else:
            root.right = self.insert(root.right,data)
        return root

    def preorder(self,root):
       print(root.val,end=" ")
       self.preorder(root.left)
       self.preorder(root.right)

    def inorder(self,root):
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def postorder(self,root):
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")