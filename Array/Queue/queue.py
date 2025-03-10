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
    STEP 2: IF FRONT and REAR is -1 THEN GO TO STEP 3 ELSE Go to step 4
    STEP 3: return TRUE
    STEP 4: return FALSE
    STEP 5: END
    """
    if FRONT and REAR is -1:
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
    pass


def front() -> int:
    """
    STEP 1: START
    STEP 2: IF not is_empty() THEN Go to STEP 3
    STEP 3: return the element at FRONT
    STEP 4: END
    """
    pass


def enqueue():
    """
    STEP 1: START
    STEP 2: Receive the element to be inserted.
    STEP 3: IF not is_full() THEN Go to 4 ELSE Go to 6.
    STEP 4: Increment the REAR Pointer.
    STEP 5: Store the element at REAR Location.
    STEP 6: return overflow message.
    """
    pass


def dequeue():
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
    pass
