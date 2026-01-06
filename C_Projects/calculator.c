#include <stdio.h>

int main(){
    float a, b;
    float result;
    int choice;
    float sum, subtract, multiply, division;

    printf("\n");
    //intro 
    printf("***<>***<>***<>***<>***<>***<>***<>");
    printf("\n    Welcome to Calculator\n");
    printf("***<>***<>***<>***<>***<>***<>***<>");
    printf("\n");
    
    printf("Input The Number\n");
    printf("Number 1 = ");
    if(scanf("%f", &a) != 1){
        printf("Invalid Input");
    }
    printf("Number 2 = ");
    if(scanf("%f", &b) != 1){
        printf("Invalid Input");
    }
    
    printf("\n--------");
    printf("\n  MENU:\n");
    printf("--------\n");
    printf("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n");

    //taking the input from the user to perfrom operation
    
    printf("Choose ->\t");
    if(scanf("%d", &choice) != 1){
        printf("\nInvalid Input\n");
    }
    sum = a + b;
    subtract = a-b;
    multiply = a*b;
    division = a/b;

    switch(choice){
        case 1: printf("The Answer is =%.2f", sum);
        break;
        case 2: printf("The Answer is=%.2f", subtract);
        break;
        case 3: printf("The Answer is=%.2f", multiply);
        break;
        case 4: printf("The Answer is=%.2f", division);
        break;
        default: printf("Invalid Number");

    }
    return 0;
}