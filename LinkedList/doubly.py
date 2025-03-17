class Node:
    def __init__(self, value):
        self.pre = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def main(self):
        while True:
            choice = int(input("1.Insert\n2.Search\n3.Delete\n4.Display\n5.Exit\nEnter your choice: "))
            if choice == 1:
                self.insert()
            elif choice == 2:
                self.search()
            elif choice == 3:
                self.delete()
            elif choice == 4:
                self.display()
            elif choice == 5:
                return False
            else:
                print("Choose from above option only!")

    def insert(self):
        """
        1) Algorithm to add element at head.
        Step 1: Start
        Step 2: Ask for value
        Step 3: set new_node = Node(value) , initialize the new node
        Step 4: IF head == Null , if head is null do the step 5 and return else go to step 6
        Step 5: head = new_node
        Step 6: new_node.left = head
        Step 8: head.right = new_node
        Step 9: head = new_node
        Step 10: END
        """
        value = int(input("Enter the Value to be Added:- "))
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return print("Added to the head.")
        choice = int(input("1.At Head\n2.At Somewhere in Middle\n3.At End\nEnter your choice: "))
        if choice == 1:
            self.head(new_node)
            print("Successes")
        elif choice == 2:
            loc = int(input("Enter the location: "))
            self.__insert_at_loc(loc, new_node)
            print("Successes")
        elif choice == 3:
            self.__insert_at_tail(new_node)
            print("Successes")
        else:
            print("Wrong Choice Try Again")

    def __insert_at_head(self, new_node):
        new_node.left = self.head
        self.head.pre = new_node
        self.head = new_node

    def __insert_at_loc(self, loc, new_node):
        if loc == 1:
            new_node.left = self.head
            self.head.left.pre = new_node
            self.head = new_node
        cnt = 1
        tmp = self.head
        while tmp.left is not None and cnt < loc:
            tmp = tmp.next
            cnt += 1
        if tmp.left is not None:
            new_node.left = tmp.left
            tmp.left.pre = new_node

        new_node.pre = tmp
        tmp.left = new_node

    def __insert_at_tail(self, new_node):
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.left
        tmp.next = new_node
        new_node.pre = tmp

    def delete(self):
        if self.head is None:
            return print("No Nodes Available")
        choice = int(input("1.Delete Head\n2.Delete Any\n3.Delete End\nEnter your choice: "))
        if choice == 1:
            self.__delete_head()
            print("Success")
        elif choice == 2:
            loc = int(input("Enter the location: "))
            self.__delete_at_location(loc)
            print("Success")
        elif choice == 3:
            self.__delete_tail()
            print("Success")

    def __delete_head(self):
        if self.head.left is None:
            self.head = None
        else:
            self.head.left.pre = None
            self.head = self.head.left

    def __delete_tail(self):
        tmp = self.head
        while tmp.left.left is not None:
            tmp = tmp.left
        tmp.left = None

    def __delete_at_location(self, loc):
        if loc == 1:
            self.__delete_head()
        cnt = 1
        tmp = self.head
        while tmp is not None and cnt < loc:
            tmp = tmp.left
            cnt += 1
        if tmp is None or tmp.left is None:  # If out of bounds
            print("Location out of bounds!")
            return
        node_to_be_deleted = tmp.left
        tmp.left = node_to_be_deleted.left
        if node_to_be_deleted.left is not None:
            node_to_be_deleted.left.pre = tmp

    def search(self):
        if self.head is None:
            return print("Head is Null")
        value = int(input("Enter the value to be searched: "))
        tmp = self.head
        while tmp is not None:
            if tmp.value == value:
                return print("Element Found")
            tmp = tmp.left
        print("Element Notfound!")

    def display(self):
        if self.head is None:
            return print("Head is Null")
        choice = int(input("1.Forward\n2.Backward\nEnter your Choice: "))
        if choice == 1:
            self.__display_forward()
        elif choice == 2:
            self.__display_backward()
        else:
            print("Oops Wrong Choice!")

    def __display_forward(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end="<->")
            tmp = tmp.left

    def __display_backward(self):
        tmp = self.head
        while tmp.left is not None:
            tmp = tmp.left

        while tmp is not None:
            print(tmp.value, end="<->")
            tmp = tmp.pre


if __name__ == "__main__":
    dd = DoublyLinkedList()
    dd.main()
