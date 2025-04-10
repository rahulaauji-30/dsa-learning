class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self):
        if self.top == 5:
            return print('Overflow')
        value = int(input("Enter the value: "))
        self.top += 1
        self.stack.append(value)

    def pop(self):
        if self.top == -1:
            return print("Underflow.")
        print(self.stack.pop())
        self.top -= 1

    def peek(self):
        return print(f"\nTop: {self.stack[self.top]}")

    def main(self):
        while True:
            choice = int(input("\n1.Push\n2.Pop\n3.Top\n4.Exit\n"
                               "Enter your choice: "))
            if choice == 1:
                self.push()
            elif choice == 2:
                self.pop()
            elif choice == 3:
                self.peek()
            elif choice == 4:
                exit()
            else:
                print("Choose from above options only.")


if __name__ == "__main__":
    stack = Stack()
    stack.main()
