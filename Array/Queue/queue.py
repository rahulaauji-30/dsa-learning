"""
Queue is Linear datastructures which allows insertion and deletion of the element only from one end.
It follows First In First Out principle.It has following three types.
1) Circular Queue
2) Priority Queue
3) Double Ended Queue (Dequeue)
It contains REAR and FRONT. The elements are inserted from the REAR and deleted from the FRONT.
It has the following operations associated:
1) Enqueue - Insert element in the queue.
2) Dequeue - Delete element form the queue.
3) Front - Returns the front element without removing.
4) isEmpty - Checks if the queue is empty or not.
5) isFull - Checks if the queue is Full or not.
"""

QUEUE = []
MAX = 10
FRONT = -1
REAR = -1


def is_empty() -> bool:
    """
    STEP 1: START
    STEP 2: IF REAR is -1 THEN GO TO STEP 3 ELSE Go to step 4
    STEP 3: return TRUE
    STEP 4: return FALSE
    STEP 5: END
    """
    if REAR == -1:
        return True
    return False


def is_full() -> bool:
    """
    STEP 1: START
    STEP 2: IF FRONT is MAX THEN Go to STEP 3 ELSE Go to STEP 4
    STEP 3: return TRUE
    STEP 4: return FALSE
    STEP 5: END
    """
    if REAR < MAX:
        return False
    return True


def front():
    """
    STEP 1: START
    STEP 2: IF not is_empty() THEN Go to STEP 3
    STEP 3: return the element at FRONT
    STEP 4: END
    """
    if is_empty():
        return print("Queue is empty.")
    return print(QUEUE[FRONT])


def enqueue():
    """
    STEP 1: START
    STEP 2: Receive the element to be inserted.
    STEP 3: IF not is_full() THEN Go to 4 ELSE Go to 6.
    STEP 4: Increment the REAR Pointer.
    STEP 5: Store the element at REAR Location.
    STEP 6: return overflow message.
    """
    global REAR
    if is_full():
        return print("The Queue is full.")

    value = int(input("Enter the value: "))
    if REAR < MAX:
        REAR += 1
        QUEUE.append(value)
        print("Added to Queue.")


def dequeue():
    global FRONT, REAR
    """
    STEP 1: START
    STEP 2: IF is_empty THEN go to 3 ELSE go to 4
    STEP 3: return Empty message
    STEP 4: print the element stored at FRONT location.
    STEP 5: increment the FRONT pointer
    STEP 6: IF FRONT == REAR THEN go to 7
    STEP 7: SET FRONT AND REAR = -1
    STEP 8: END
    """
    if is_empty():
        return print("Queue is empty!")
    else:
        FRONT += 1
        print(f"\nRemoved {QUEUE[FRONT]}")
    if FRONT > REAR:
        FRONT = -1
        REAR = -1


def display():
    for item in QUEUE:
        print(item)


def main():
    choice = int(input("\n1.Enqueue\n2.Dequeue\n3.Is Full\n4.Is Empty\n5.Peek\n6.Display\nEnter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        is_full()
    elif choice == 4:
        is_empty()
    elif choice == 5:
        front()
    elif choice == 6:
        display()
    else:
        print("Choose from above options only!")


if __name__ == "__main__":
    while True:
        main()
