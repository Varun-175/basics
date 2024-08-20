#include<stdio.h>
#include<stdlib.h>

int stack[100], choice, size, top, x, i;

void push();
void pop();
void display();

int main() 
{
    
    top = -1;
        printf("\nEnter the size of STACK (1 to 100): "); 
    scanf("%d", &size);
    if (size<=0 || size>100) 
    {
        printf("\nInvalid size! Please enter a size between 1 and 100.\n");
    }

    printf("\nSTACK OPERATIONS USING ARRAY\n");
    printf("\n\t1. Push\n\t2. Pop\n\t3. Display\n\t4. Exit\n"); 

    while(1) 
    {
        printf("\n\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice) 
        {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                printf("\nExiting program...\n\n");
                exit(0);
            default:
                printf("\nInvalid Choice! Please enter a valid choice (1/2/3/4).\n");
                break;
        }
    }

    return 0;
}

void push() 
{
    if (top>=size-1) 
    {
        printf("\nSTACK overflow!\n");
    } 
    else 
    {
        printf("\nEnter a value to be pushed: ");
        scanf("%d", &x);
        top++;
        stack[top] = x;
        printf("\nValue %d pushed onto stack.\n", x);
    }
}

void pop() 
{
    if (top <= -1) 
    {
        printf("\nSTACK underflow!\n");
    } 
    else 
    {
        printf("\nThe popped element is %d\n", stack[top]);
        top--;
    }
}

void display() 
{
    if (top >= 0) 
    {
        printf("\nThe elements in STACK:\n");
        for (i = top; i >= 0; i--) 
        {
            printf("\n\t%d", stack[i]);
        }
    } 
    else 
    {
        printf("\nThe STACK is empty.\n");
    }
}
