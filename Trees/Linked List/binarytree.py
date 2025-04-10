class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self):
        value = int(input("Enter the value : "))
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            tmp = self.root
            parent = None
            while tmp is not None:
                parent = tmp
                if tmp.value == value:
                    return print("Duplicate Value is not allowed.")
                elif tmp.value > value:
                    tmp = tmp.left
                else:
                    tmp = tmp.right
            if parent.value > value:
                parent.left = new_node
            elif parent.value < value:
                parent.right = new_node

    def delete(self):
        if self.root is None:
            return print("Tree is empty!")

        value = int(input("Enter the value to delete: "))
        tmp = self.root
        parent = None
        # Step 1: Find the node to delete and track its parent
        while tmp is not None and tmp.value != value:
            parent = tmp
            if tmp.value > value:
                tmp = tmp.left
            else:
                tmp = tmp.right

        # If the value is not found
        if tmp is None:
            return print("Value Not found.")

        # Step 2: Case 1 - Node has no children (Leaf Node)
        if tmp.left is None and tmp.right is None:
            if parent is None:
                self.root = None
            elif parent.left == tmp:
                parent.left = None
            else:
                parent.right = None
        # Step 3: Case 2 - Node has One Child
        elif tmp.left is None:
            if parent is None:
                self.root = tmp.right
            elif parent.left == tmp:
                parent.left = tmp.right
            else:
                parent.right = tmp.right
        elif tmp.right is None:
            if parent is None:
                self.root = tmp.left
            elif parent.right == tmp:
                parent.right = tmp.left
            else:
                parent.right = tmp.left
        else:
            successor_parent = tmp
            successor = tmp.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            tmp.value = successor.value
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        print(f"Node with value {value} deleted successfully!")

    def __preorder(self, node):
        """
        Node Left Right
        """
        if node:
            print(node.value, end=" ")
            self.__preorder(node.left)
            self.__preorder(node.right)

    def __inorder(self, node):
        """
        Left Node Right
        """
        if node:
            self.__inorder(node.left)
            print(node.value, end=" ")
            self.__inorder(node.right)

    def __postorder(self, node):
        """
        Right Left Node
        """
        if node:
            self.__postorder(node.right)
            self.__postorder(node.left)
            print(node.value, end=" ")

    def display_tree(self):
        if self.root is None:
            print("Tree is empty!")
            return

        while True:
            print("\n--- Tree Traversal Menu ---")
            print("1. Inorder Traversal")
            print("2. Preorder Traversal")
            print("3. Postorder Traversal")
            print("4. Back to Main Menu")
            choice = input("Enter choice: ")

            if choice == '1':
                print("\nInorder Traversal: ", end="")
                self.__inorder(self.root)
                print()
            elif choice == '2':
                print("\nPreorder Traversal: ", end="")
                self.__preorder(self.root)
                print()
            elif choice == '3':
                print("\nPostorder Traversal: ", end="")
                self.__postorder(self.root)
                print()
            elif choice == '4':
                break
            else:
                print("Invalid choice! Please enter a valid option.")

    def main(self):
        while True:
            print("\n--- Binary Tree Menu ---")
            print("1. Insert")
            print("2. Delete")
            print("3. Display Tree")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.insert()
            elif choice == '2':
                self.delete()
            elif choice == '3':
                self.display_tree()
            elif choice == '4':
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    bt = BinaryTree()
    bt.main()
