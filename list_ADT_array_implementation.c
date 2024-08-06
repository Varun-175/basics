#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void create();
void insert();
void deletion();
void search();
void remove_duplicate();
void display();
int arr[MAX], size,i,j,k;

void main() 
{
    int num;
    char g = 'y';

    do {
        printf("\nMain Menu\n");
        printf("\n1. Create\n2. Delete\n3. Search\n4. Insert\n5. Display\n6. Remove Duplicate\n7. Exit\n");
        printf("\nEnter your choice: ");
        scanf("%d", &num);

        switch (num) {
            case 1:
                create();
                break;
            case 2:
                deletion();
                break;
            case 3:
                search();
                break;
            case 4:
                insert();
                break;
            case 5:
                display();
                break;
            case 6:
                remove_duplicate();
                break;
            case 7:
                return;
            default:
                printf("\nEnter the correct choice.");
        }
        printf("\nDo you want to continue (y/n): ");
        scanf(" %c", &g); 
    } while (g == 'y' || g == 'Y');
}

void create() {
    printf("\nEnter the number of elements: ");
    scanf("%d", &size);

    if (size > MAX) {
        printf("Number of elements exceeds maximum limit of %d\n", MAX);
        size = MAX;
    }

    for (i = 0; i < size; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }
    display();
}

void deletion() {
    int pos;
    printf("\nEnter the position you want to delete: ");
    scanf("%d", &pos);

    if (pos >= size || pos < 0) {
        printf("\nInvalid location.");
    } 
    else {
        for (i = pos; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        size--;
        printf("\nThe elements after deletion:");
        display();
    }
}

void search() {
    int element;
    printf("\nEnter the element to be searched: ");
    scanf("%d", &element);

    for (i = 0; i < size; i++) {
        if (arr[i] == element) {
            printf("Value is at position %d\n", i);
            return;
        }
    }
    printf("Value %d is not in the list.\n", element);
    display();
}

void insert() {
    int pos, element;
    printf("\nEnter the position you need to insert: ");
    scanf("%d", &pos);

    if (pos > size || pos < 0 || size == MAX) {
        printf("\nInvalid location or list is full.");
    } else {
        for (i = size; i > pos; i--) {
            arr[i] = arr[i - 1];
        }
        printf("\nEnter the element to insert: ");
        scanf("%d", &element);
        arr[pos] = element;
        size++;
        printf("\nThe list after insertion:");
        display();
    }
}

void remove_duplicate() {
    for(i=0;i<size;i++){
        for(j = i+1; j < size; j++){
            if(arr[i] == arr[j]){
                printf("\nThe duplicate element is: %d",arr[i]);
                for(k = j; k <size; k++){
                    arr[k] = arr[k+1];
                }
                j--;
                size--;
            }
        }
    }
    printf("\nAfter deletion: \n");
    display();
}

void display() {
    printf("\nThe elements of the list new are:");
    for (int i = 0; i < size; i++) {
        printf("\n%d", arr[i]);
    }
    printf("\n");
}