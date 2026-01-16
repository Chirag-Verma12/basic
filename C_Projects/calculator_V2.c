#include <stdio.h>
#include <ctype.h>

int main(){
    float a, b;
    int choice;
    char again;
    float result;
    char invalid;
    char invalid_n2;

    printf("\n");
    //intro 
    printf("***<>***<>***<>***<>***<>***<>***<>");
    printf("\n    Welcome to Calculator\n");
    printf("***<>***<>***<>***<>***<>***<>***<>");
    printf("\n");
    printf("\n");
    printf("     Instruction :");
    printf("\n=======================");
    printf("\nIf you enter an alpabet the code will crash");
    printf("\n");

    //right now we are testing things on 'a' but we have to do it on the scanf 
    //so, try all the method if(scanf("%f", &a) != isalpha(a)) all that or != 'y' etc etc
    do{
        do {
            printf("\nNumber 1: ");

            if (scanf("%f", &a) != 1) {   // 👈 detects character input
                printf("\nInvalid Input!");

            // clear input buffer
            while (getchar() != '\n');
            printf("\nWanna try again? (y/n): ");
            scanf(" %c", &invalid);
        } else if (a < 1) {             // number but invalid range
            printf("\nInvalid Input! Number must be >= 1");
            printf("\nWanna try again? (y/n): ");
            scanf(" %c", &invalid);
        } else {
        break; // valid number
        }
    } while (invalid == 'y' || invalid == 'Y');
    if (invalid == 'n' || invalid == 'N') {
        break;
    }       

    do{
        printf("\nNumber 2:");

        if(scanf("%f", &b) != 1){
            printf("\nInvalid Number");

            while(getchar() != '\n');
            printf("\nWanna try again? (y/ n): ");
            scanf(" %c", &invalid_n2);
        } else if(b < 1){
            printf("\nInvalid Input ! Number must be >= 1");
            printf("Wanna try again? (y/ n): ");
            scanf(" %c", &invalid_n2);
        } else{
            break;
        } 
    }while(invalid_n2 == 'y' || invalid_n2 == 'Y');
    if(invalid_n2 == 'n' || invalid_n2 == 'N'){
            break;
        }
    
        printf("\n--------");
        printf("\n  MENU:\n");
        printf("--------\n");
        printf("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n");

        //taking the input from the user to perfrom operation
    
        printf("Choose ->\t");
        if(scanf("%d", &choice) != 1){
            printf("\nInvalid Input\n");
            break;
        }

        switch(choice){
            case 1: 
            result = a + b;
            printf("\nThe Answer is =%.2f", result);
            break;
            case 2: 
            result = a-b;
            printf("\nThe Answer is=%.2f", result);
            break;
            case 3: 
            result = a*b;
            printf("\nThe Answer is=%.2f", result);
            break;
            case 4: 
            if(b == 0){
                printf("\nInvalid Input\n");
                break;
            }
            result = a/b;
            printf("The Answer is=%.2f", result);
            break;
            default: printf("\nInvalid Number\n");
        }
        printf("\n");
        printf("\nDo u want to do again? (y/ n) ->\t");
        scanf(" %c", &again);
        if(again == 'n' || again == 'N'){
            printf("\n-+-+-+-+-+-+-+-+-+-+-+-+");
            printf("\n       Thank you");
            printf("\n-+-+-+-+-+-+-+-+-+-+-+-+");
        }
    } while(again == 'y' || again == 'Y');
    return 0;
}