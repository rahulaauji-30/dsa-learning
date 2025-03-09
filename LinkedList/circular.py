class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def main(self):
        while True:
            choice = int(input("1.Insert\n2.Delete\n3.Display\n4.Exit\nEnter your choice: "))
            if choice == 1:
                self.insert()
            elif choice == 2:
                self.delete()
            elif choice == 3:
                self.display()
            elif choice == 4:
                return False
            else:
                print("Choose from above option only!")

    def insert(self):
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
            self.__insert_tail(new_node)
            print("Successes")
        else:
            print("Wrong Choice Try Again")

    def __insert_head(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def __insert_tail(self, new_node):
        tmp = self.head

        while tmp.next is not self.head:
            tmp = tmp.next

        new_node.next = tmp.next
        tmp.next = new_node

    def __insert_at_loc(self, loc, new_node):
        if loc <= 0:
            return print("Invalid Index Range!")
        if loc == 1:
            self.__insert_head(new_node)
            return

        cnt = 1
        tmp = self.head
        while tmp.next is not self.head and cnt < loc:
            tmp = tmp.next
            cnt += 1
        new_node.next = tmp.next
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
        if self.head.next is None:
            self.head = None
        else:
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = self.head.next
            self.head = self.head.next

    def __delete_tail(self):
        if self.head.next is None:
            self.head = None
            return

        tmp = self.head
        while tmp.next.next is not self.head:
            tmp = tmp.next
        tmp.next = self.head

    def __delete_at_location(self, loc):
        if loc == 1:
            self.__delete_head()
            return
        cnt = 1
        tmp = self.head
        while tmp.next is not self.head and cnt < loc - 1:
            tmp = tmp.next
            cnt += 1
        if tmp.next == self.head:
            print("Location out of bounds!")
            return
        tmp.next = tmp.next.next

    def display(self):
        if self.head is None:
            return print("Head is Null.")
        tmp = self.head
        while tmp is not self.head:
            print(tmp.value, end="->")
            tmp = tmp.next


if __name__ == "__main__":
    c = CircularLinkedList()
    c.main()
