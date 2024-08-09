#include<stdio.h>
#include<math.h>

int main(){

    int a,size;
    printf("\nEnter the main number: ");
    scanf("%d",&a);
    printf("\nEnter the size of the array: ");
    scanf("%d",&size);
    int arr[size];
    for(int i=0;i<size;i++){
        printf("\nEnter element-[%d]: ",i+1);
        scanf("%d",&arr[i]);
    }
    int temp=0;
    for(int i=0;i<size;i++){
        
        if (arr[i]!=0){
            temp *= 10;
            temp += arr[i];
        }
        else{
            temp += arr[i];
        }
    }
    int result = pow(a,temp);
    printf("\nResult: %d\n",result);
    return 0;    

}