class Node:
    def __init__(self, value):
        self.pre = None
        self.value = value
        self.next = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def main(self):
        while True:
            choice = int(input("\n1.Insert\n2.Search\n3.Delete\n4.Display\n5.Exit\nEnter your choice: "))
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
        value = int(input("Enter the Value to be Added:- "))
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.head.pre = new_node
            return print("Added to the head.")
        choice = int(input("1.At Head\n2.At Somewhere in Middle\n3.At End\nEnter your choice: "))
        if choice == 1:
            self.__insert_head(new_node)
            print("Successes")
        elif choice == 2:
            loc = int(input("Enter the location: "))
            self.__insert_at_location(loc, new_node)
            print("Successes")
        elif choice == 3:
            self.__insert_tail(new_node)
            print("Successes")
        else:
            print("Wrong Choice Try Again")

    def __insert_head(self, new_node):
        last = self.head.pre
        new_node.left = self.head
        new_node.pre = last
        self.head.pre = new_node
        last.left = new_node
        self.head = new_node

    def __insert_tail(self, new_node):
        tail = self.head.pre
        tail.left = new_node
        new_node.pre = tail
        new_node.left = self.head
        self.head.pre = new_node

    def __insert_at_location(self, loc, new_node):
        if loc == 1:
            self.__insert_head(new_node)
            return
        cnt = 1
        tmp = self.head
        while tmp.next is not self.head and cnt < loc - 1:  # 1-> 2->4-> 3
            tmp = tmp.left
            cnt += 1
        new_node.left = tmp.next
        tmp.next.pre = new_node
        new_node.pre = tmp
        tmp.next = new_node

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
        if self.head.left is self.head:
            self.head = None
            return
        node_to_delete = self.head
        new_head = node_to_delete.left
        tail = node_to_delete.pre
        new_head.pre = tail
        tail.left = new_head
        self.head = new_head
        del node_to_delete

    def __delete_tail(self):
        if self.head.left is self.head:
            self.head = None
            return
        tail = self.head.pre
        new_tail = tail.pre
        new_tail.left = self.head
        self.head.pre = new_tail
        del tail

    def __delete_at_location(self, loc):
        if loc <= 0:
            return print("Index Out of bound.")

        if loc == 1:
            self.__delete_head()
            return
        cnt = 1
        tmp = self.head
        while tmp.left is not self.head and cnt < loc - 1:
            tmp = tmp.left
        node_to_delete = tmp.left
        next_node = node_to_delete.left
        if next_node == self.head:
            tmp.left = self.head
            self.head.pre = tmp
        else:
            tmp.left = next_node
            next_node.pre = tmp
        del node_to_delete

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
        while True:
            print(tmp.value, end="<->")
            tmp = tmp.left
            if tmp is self.head:
                break
        print("<HEAD>")

    def __display_backward(self):
        tmp = self.head.pre
        while True:
            print(tmp.value, end="<->")
            tmp = tmp.pre
            if tmp is self.head.pre:
                break
        print("<HEAD>")

    def search(self):
        value = int(input("Enter the value to be searched: "))
        tmp = self.head
        while tmp.left is not self.head:  #1->2->3->4
            if tmp.value == value:
                print("Element Found")
                return
            tmp = tmp.left
        print("Element Not Found!")


if __name__ == "__main__":
    dc = DoublyCircularLinkedList()
    dc.main()
