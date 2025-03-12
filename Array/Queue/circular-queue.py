QUEUE = []
CAPACITY = 5
REAR = -1
FRONT = -1


def is_empty():
    if REAR == -1:
        return True
    return False


def get_front():
    if is_empty():
        return print("Queue is empty.")

    print(QUEUE[FRONT])


def get_rear():
    if is_empty():
        return print("Queue is empty.")
    print(QUEUE[REAR])


def enqueue():
    global FRONT, REAR, QUEUE

    if (REAR + 1) % CAPACITY == FRONT:
        print("Queue is Full!")
        return

    value = int(input("Enter the element to be stored: "))

    if FRONT == -1:
        FRONT = 0

    REAR = (REAR + 1) % CAPACITY
    if len(QUEUE) < CAPACITY:
        QUEUE.append(value)
    else:
        QUEUE[REAR] = value
    print(f"Inserted {value} at position {REAR}")


def dequeue():
    global FRONT, REAR
    if FRONT == -1:
        return print("Queue is empty!")
    value = QUEUE[FRONT]
    print(f"Dequeued {value} from position {FRONT}")
    if FRONT > CAPACITY-1:
        FRONT = 0
    if FRONT == REAR:
        FRONT = REAR = -1
    else:
        FRONT = (FRONT + 1) % CAPACITY


def display():
    global FRONT, REAR, QUEUE

    if FRONT == -1:  # Queue Empty Condition
        print("Queue is Empty!")
        return

    print("Circular Queue: ", end="")

    i = FRONT
    while True:
        print(QUEUE[i], end=" ")
        if i == REAR:  # Stop when reaching the REAR
            break
        i = (i + 1) % CAPACITY  # Move circularly

    print()  # New line for clean output


def main():
    while True:
        print("\nCircular Queue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            print("Exiting... 🚀")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
