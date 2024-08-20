#include<stdio.h>
#include<stdlib.h>

void create();
void display();
void insert_at_begin();
void insert_at_position();
void insert_at_end();
void deletion();

struct node
{
    int data;
    struct node *next;
};

struct node *head=NULL;

int main()
{
    int choice;
    printf("\n\tMain Menu\n");
    printf("\n\t1.Create\n\t2.Display\n\t3.Insert at Beginning\n\t4.Insert at Position\n\t5.Insert at Ending\n\t6.Delete\n\t7.Exit\n");
    while(1)
    {
        printf("\nEnter your choice: \n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
                create();
                break;
            case 2:
                display();
                break;
            case 3:
                insert_at_begin();
                break;
            case 4:
                insert_at_position();
                break;
            case 5:
                insert_at_end();
                break;
            case 6:
                deletion();
                break;
            case 7:
                printf("Exiting program...");
                exit(0);
                break;
            default:
                printf("\nInvalid choice, Please try again.\n");
        }
    }
    return 0;
}

void create()
{
    int data;
    printf("\nEnter data to insert: ");
    scanf("%d",&data);
    struct node *temp,*ptr;
    temp=(struct node*)malloc(sizeof(struct node));
    if(temp==NULL)
    {
        printf("Memory is not allocated.\n");
        exit(0);
    }
    else
    {
        temp->data=data;
        temp->next=NULL;
    }
    if(head==NULL)
        head=temp;
    else
    {
        ptr=head;
        while(ptr->next!=NULL)
        {
            ptr=ptr->next;
        }
        ptr->next=temp;
    }
}

void insert_at_begin()
{
    int data;
    printf("\nEnter data to insert at the beginning: ");
    scanf("%d",&data);
    struct node *temp;
    temp=(struct node*)malloc(sizeof(struct node));
    temp->data=data;
    temp->next=head;
    head=temp;
}

void insert_at_position()
{
    int data, pos, i;
    printf("\nEnter data to insert: ");
    scanf("%d",&data);
    printf("\nEnter the position to insert at: ");
    scanf("%d",&pos);

    struct node *temp=(struct node*)malloc(sizeof(struct node));
    if (pos==1) 
    {
        temp->next=head;
        head=temp;
        printf("\nNode with data %d inserted at position %d.\n", data, pos);
        return;
    }

    struct node *ptr = head;
    for (i=1;i < pos-1;i++) 
    {
        if (ptr == NULL) 
        {
            printf("\nPosition out of bounds. Node not inserted.\n");
            return;
        }
        ptr=ptr->next;
    }
    if (ptr == NULL)
        printf("\nPosition out of bounds. Node not inserted.\n"); 
    else 
    {
        temp->data=data;
        temp->next=ptr->next;
        ptr->next=temp;
        printf("\nNode with data %d inserted at position %d.\n", data, pos);
    }
}

void insert_at_end()
{
    int data;
    printf("\nEnter data to insert at the ending: ");
    scanf("%d",&data);
    struct node *temp=head,*ptr=(struct node*)malloc(sizeof(struct node));
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    ptr->data=data;
    ptr->next=NULL;
    temp->next=ptr;
}

void deletion()
{
    int data;
    printf("\nEnter the data to be deleted: ");
    scanf("%d",&data);
    struct node *temp=head;
    while(((temp->next)->data!=data) && (temp->next)!=NULL)
    {
        temp=temp->next;
    }
    if(temp->next==NULL)
    {
        printf("\n%d is not found in this list.\n",data);
    }
    else
    {
        struct node *z=temp->next;
        temp->next=(temp->next)->next;
        free(z);
        printf("\nThe element %d is deleted from the list.",data);
    }
}

void display()
{
    struct node *ptr;
    if(head==NULL)
    {
        printf("\nList is empty!\n");
        return;
    }
    else
    {
        printf("\nLinked List: \n");
        ptr=head;
        while(ptr!=NULL)
        {
            printf(" %d->",ptr->data);
            ptr=ptr->next;
        }
        printf("NULL\n");
    }
}
