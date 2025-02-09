#include <stdio.h>
int stack[10];
int top=-1;
/*
 Stack is a linear Data Structure which follows Last In First Out order.
 It has following operations:
 1) Push
 2) Pop
 3) Peek
 4) Display
*/

void push(){
    if(top==10){
        printf("\nCan't Add One more element.");
        return;
    }
    printf("\nEnter the element to be added:- ");
    scanf("%d",&stack[++top]);
}

void pop(){
    if(top==-1){
        printf("\nCan't Pop as it's Empty.");
        return;
    }
    printf("\nRemoved %d",stack[top--]);
}

void peek(){
    if (top==-1)
    {
        printf("\nStack is empty.");
        return;
    }
    printf("\nTopmost element is %d",stack[top]);
}

void display(){
    if (top==-1)
    {
        printf("\nStack is empty.");
        return;
    }
    for (int i = 0; i <= top; i++)
    {
        printf("\n%d",stack[i]);
    }
    
}

int main(){
    int choice;
    while(1){
        printf("\nSelect the following Operations:\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit\nEnter your Choice here: ");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:push();
            break;
        case 2:pop();
        break;
        case 3:peek();
        break;
        case 4:display();
        break;
        case 5:return 0;
        default:printf("\nPlease select the from given options!");
            break;
        }
    }
    return 0;
}