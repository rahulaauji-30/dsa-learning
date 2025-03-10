/*
    Linked List is collection of data elements stored in such a manner that each elements point to the next element int the list.
    It has following operations:-
    1) Insert
    2) Delete
    3) Display
*/
#include<stdio.h>

struct node{
    int data;
    struct node *next;
};
struct node *head=NULL,*tmp;

void insert();
void delete();
void search();
void display();

void main(){
    int choice;
    while(1){
        switch(choice){
            case 1:insert();
            break;
            case 2:delete();
            break;
            case 3:search();
            break;
            case 4:display();
            break;
            default: printf("Please select from given options only!");
        }
    }
}

void insert(){
    /*
    step 1: Start
    step 2: Check if the head is null or not if not continue else go to step 
    step 3: Allocate memory for the new node 
    step 4: assign the data part a value. 
    step 5: point the next part to the null 
    step 6: Set the head to the new node (Skip this step if head!=null)
    step 7: Stop
    */
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    int choice;
    printf("Enter the number to be inserted: ");
    scanf("%d",&newNode->data);
    newNode->next = NULL;
    if(head==NULL){
        head = newNode;
    }else{
        tmp = newNode;
        printf("\n1.Head\n2.End\n3.Any\nWhere do you want to add the element: ");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1: tmp->next = head;
                head = tmp;
            break;
        case 2: 
        
        default:
            break;
        }
    }

}