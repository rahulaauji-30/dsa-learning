class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [-1] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def insert_front(self, value):
        if self.is_full():
            print("Queue is full.")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity

        self.queue[self.front] = value
        print(f"Inserted {value} at front.")

    def insert_rear(self, value):
        if self.is_full():
            print("Queue is full.")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = value
        print(f"Inserted {value} at rear.")

    def delete_front(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print(f"Removed {self.queue[self.front]} from front.")
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset when last element is removed
        else:
            self.front = (self.front + 1) % self.capacity

    def delete_rear(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print(f"Removed {self.queue[self.rear]} from rear.")
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

    def get_front(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Front: {self.queue[self.front]}")

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Rear: {self.queue[self.rear]}")

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Deque:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


def main():
    dq = Deque()

    while True:
        print("\n1.Insert Front\n2.Insert Rear\n3.Delete Front\n4.Delete Rear\n5.Get Front\n6.Get "
              "Rear\n7.Display\n8.Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            dq.insert_front(int(input("Enter value: ")))
        elif choice == 2:
            dq.insert_rear(int(input("Enter value: ")))
        elif choice == 3:
            dq.delete_front()
        elif choice == 4:
            dq.delete_rear()
        elif choice == 5:
            dq.get_front()
        elif choice == 6:
            dq.get_rear()
        elif choice == 7:
            dq.display()
        elif choice == 8:
            exit()
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
