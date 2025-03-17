class Stack:
    """
    Stack follows LIFO, It has the following functions:
    1) Push - It adds elements at the top of the stack
    2) Pop - It removes the elements from the stack.
    3) Peek - It returns the top most element of the stack
    4) is_Empty - It checks if the stack is empty or not
    5) is_Full - It checks if the stack is full or not
    """

    def __init__(self):
        self.stack = []
        self.top = -1

    def __is_empty(self) -> bool:
        if self.top == -1:
            return True
        else:
            return False

    def __is_full(self):
        if self.top > 9:
            return True
        else:
            return False

    def __push(self):
        if self.__is_full():
            return print("Can't proceed stack is full.")
        element = int(input("Enter the number to be added: "))
        self.stack.append(element)
        self.top += 1

    def __pop(self):
        if self.__is_empty():
            return print("Can't proceed stack is empty")

        print(f"Removed {self.stack[self.top]}")
        self.top -= 1

    def __peek(self):
        if self.__is_empty():
            return print("Can't proceed stack is empty.")
        print(self.stack[self.top])

    def main(self):

        while True:
            choice = input("1.Push\n2.Pop\n3.Peek\n4.Exit\nEnter your choice here: ")
            if choice.lower() == "push":
                self.__push()
            elif choice.lower() == "pop":
                self.__pop()
            elif choice.lower() == "peek":
                self.__peek()
            elif choice.lower() == "exit":
                return False
            else:
                print("Invalid Choice choose among the above options: ")


class StackLinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def __push(self):
        value = int(input("Enter the number to be stored: "))
        if self.__is_empty():
            self.head = self.Node(value)
        else:
            new_node = self.Node(value)
            new_node.next = self.head
            self.head = new_node
        print("Element Added Succesfully")

    def __pop(self):
        if self.__is_empty():
            return print("Stack is empty!")
        print(self.head.value)
        self.head = self.head.left

    def __peek(self):
        if self.__is_empty():
            return print("Stack is empty!")
        print(self.head.value)

    def main(self):
        while True:
            choice = input("1.Push\n2.Pop\n3.Peek\n4.Exit\nEnter your choice here: ")
            if choice.lower() == "push":
                self.__push()
            elif choice.lower() == "pop":
                self.__pop()
            elif choice.lower() == "peek":
                self.__peek()
            elif choice.lower() == "exit":
                return False
            else:
                print("Invalid Choice choose among the above options: ")
