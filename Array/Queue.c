#include <stdio.h>
#include <stdbool.h>
int FRONT = -1;
int REAR = -1;
int queue[10];

/*
    Queue is a linear data structure in which the elements are added from one end and deleted from another end. It follows First In First Out Principle. It has following operations:
    1) Insert (Enqueue)
    2) Delete (Dequeue)
    3) Display
    4) Peek
    5) isEmpty
    6) isFull
*/

void enqueue();
void dequeue();
void display();
void peek();
bool isEmpty();
bool isFull();

int main()
{
    int choice;
    while (1)
    {
        printf("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Peek\n5.Exit\nSelect the above choice:- ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            enqueue();
            break;
        case 2:
            dequeue();
            break;
        case 3:
            display();
            break;
        case 4:
            peek();
            break;
        case 5:
            return 0;
        default:
            printf("\nPlease choose from given options!");
            break;
        }
    }
}

bool isEmpty()
{
    if (REAR == -1 && FRONT == -1)
        return true;
    else
        return false;
}

bool isFull()
{
    if (REAR == 9)
        return true;
    else
        return false;
}

void enqueue()
{
    if (isFull())
    {
        printf("\nQueue is Full!");
        return;
    }
    printf("\nEnter the element to be enqueued: ");
    if (REAR == -1 && FRONT == -1)
    {
        REAR = 0;
        FRONT = 0;
        scanf("%d", &queue[REAR]);
    }
    else
        scanf("%d", &queue[++REAR]);
}

void dequeue()
{
    if (isEmpty())
    {
        printf("\nQueue is empty!");
        return;
    }
    printf("\nRemoved %d", queue[FRONT++]);

    if (FRONT > REAR)
    {
        FRONT = -1;
        REAR = -1;
    }
}

void peek()
{
    if (isEmpty())
    {
        printf("\nQueue is empty!");
        return;
    }
    printf("\nPeek Element is : %d", queue[FRONT]);
}

void display()
{
    if (isEmpty())
    {
        printf("\nQueue is empty!");
        return;
    }
    for (int i = FRONT; i <= REAR; i++)
    {
        printf("\n%d", queue[i]);
    }
}