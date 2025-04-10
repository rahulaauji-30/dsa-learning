QUEUE = []
FRONT = -1


def enqueue():
    value = int(input("Enter the value : "))
    priority = int(input("Enter the priority: "))
    QUEUE.append((value, priority))
    QUEUE.sort(key=lambda x: x[1])


def dequeue():
    global FRONT
    if not QUEUE:
        return print("Queue is empty.")
    poped_element = QUEUE.pop(0)
    print(f"Element {poped_element[0]} Priority {poped_element[1]}")


def display():
    if not QUEUE:
        return print("Queue is empty.")

    for p in QUEUE:
        print(f"Element {p[0]} and Priority {p[1]}")


def main():
    while True:
        choice = int(input("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\nEnter Your choice: "))
        if choice == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("Choose from given options only.")


if __name__ == "__main__":
    main()
