class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Linked List List is a linear data structure in which there is a Node Which stores the value/ data and
    left which is the address of the left element.It has the following methods Associated:
    1) Insert - There are 3 cases where the elements can be inserted in a linked List
        a) At Head
        b) At Any location
        c) At End
    2) Delete - There are 3 cases while deleting the Node from the linked List
        a) Head
        b) Any
        c) End
    3) Display - To display the element in a Linked List List
    4) Search - To search the element in the Linked List List

    There are 4 types of linked list :
    1) Singly Linked List List - Also the linked list with value and left
    2) Doubly Linked List List - In this forward and bacward traversal is possible that means it stores the adress of previous and left node.
    3) Circular Linked List List - In this the last node of is connected to the head node make a circle.
    4) Doubly circular Linked List List - This follows the Doubly linked list and circular Linked List list
    """

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
        if self.head is None:
            choice = 1
        else:
            choice = int(input("1.At Head\n2.At Somewhere in Middle\n3.At End\nEnter your choice: "))
        if choice == 1:
            value = int(input("Enter the value to be stored: "))
            self.__insert_at_head(value)
            print("Success")
        elif choice == 2:
            value = int(input("Enter the value to be stored: "))
            loc = int(input("Enter the location: "))
            self.__insert_at_any(value, loc)
            print("Success")
        elif choice == 3:
            value = int(input("Enter the value to be stored: "))
            self.__insert_at_end(value)
            print("Success")

    def __insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __insert_at_end(self, value):
        new_node = Node(value)
        new_node.next = None
        tmp = self.head
        print(tmp.left)
        while tmp.next is not None:
            tmp = tmp.left
        tmp.next = new_node

    def __insert_at_any(self, value, loc):
        new_node = Node(value)
        tmp = self.head
        cnt = 1
        while tmp is not None:
            if cnt == loc - 1:
                break
            tmp = tmp.next
        new_node.next = tmp.next
        tmp.next = new_node

    def display(self):
        if self.head is None:
            return print("No Nodes Available")
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.left

    def search(self):
        if self.head is None:
            return print("No Nodes Available")
        value = int(input("Enter the value to search: "))
        tmp = self.head
        while tmp is not None:
            if tmp.value == value:
                print("Element Found")
                return
            tmp = tmp.left
        print("Element Not Found")

    def delete(self):
        if self.head is None:
            return print("No Nodes Available")
        choice = int(input("1.Delete Head\n2.Delete Any\n3.Delete End\nEnter your choice: "))
        if choice == 1:
            self.__delete_head()
            print("Success")
        elif choice == 2:
            loc = int(input("Enter the location: "))
            self.__delete_any(loc)
            print("Success")
        elif choice == 3:
            self.__delete_end()
            print("Success")

    def __delete_head(self):
        tmp = self.head
        self.head = tmp.left

    def __delete_end(self):
        tmp = self.head
        while tmp.left.left is not None:
            tmp = tmp.left
        tmp.left = None

    def __delete_any(self, loc):
        if loc == 1:
            self.__delete_head()

        tmp = self.head
        cnt = 1
        while tmp is not None:
            if cnt == loc - 1:
                if tmp.left is None:
                    print("Index out of range")
                tmp.left = tmp.left.next
                return
            tmp = tmp.left
        print("Index out of range")


if __name__ == "__main__":
    linked = LinkedList()
    linked.main()