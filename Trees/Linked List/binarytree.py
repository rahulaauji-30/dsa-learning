import queue
from inspect import stack

from LinkedList.array import Queue


class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.idx = -1
        self.q = queue.Queue()

    def build_tree(self,pre_order):
        self.idx+=1
        if pre_order[self.idx] == -1:
            return None

        root = Node(pre_order[self.idx])
        root.left = self.build_tree(pre_order)
        root.right = self.build_tree(pre_order)
        return root

    def pre_order(self,root):
        if root is None:
            return

        print(root.val,end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self,root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.val,end=" ")
        self.in_order(root.right)

    def post_order(self,root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val,end=" ")

    def level_order(self,root):
        self.q.put(root)
        self.q.put(None)
        while self.q.qsize() > 0:
            current = self.q.get()

            if current is None:
                if self.q.not_empty:
                    print()
                    self.q.put(None)
                    continue
                else:
                    break
            print(current.val,end=" ")
            if current.left:
                self.q.put(current.left)
            if current.right:
                self.q.put(current.right)

    def build_tree_loops(self,pre_order):
        root = Node(pre_order[0])

        for i in range(1,len(pre_order)):
            if pre_order[i] != -1:
                new_node = Node(pre_order[i])
                while root:
                    if root.val > new_node.val:
                        parent = root.left
                    else:
                        parent = root.right

    def build_tree_stack(self,pre_order):
        if not pre_order:
            return None
        root = Node(pre_order[0])
        stack = [root]

        for i in range(1,len(pre_order)):
            if pre_order[i] == -1:
                continue
            new_node = Node(pre_order[i])
            if stack[-1].val > new_node.val:
                stack[-1].left = new_node
                stack.append(new_node)
            else:
                parent = None
                while stack and new_node.val > stack[-1].val:
                    parent = stack.pop()
                parent.right = new_node
                stack.append(new_node)
        return root
if __name__ == "__main__":
    bt = BinaryTree()
    root = bt.build_tree_stack([1, 2,-1,-1,3,4,-1,-1,5,-1,-1])
    bt.pre_order(root)
    print()
    bt.in_order(root)
    print()
    bt.post_order(root)
    print()
    bt.level_order(root)