#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<stdbool.h>

int main(){
    char choose;
    char invalid;
    bool prime;
    int number;
    char again;
    bool is_prime;
    printf("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n");
    printf("    Welcome To, Prime Number Checker/ Generator\n");
    printf("---------------------------------------------------\n");
    do{
        //generate prime number till input or check if input is prime or not
        printf("\nWhat do you wanna do,\nGenerate or Check? (g/ c):");
        scanf(" %c", &choose); 

        //checking, prime or not
        while(choose == 'c' || invalid == 'y'){
            prime = true;
            //checking if the user entered a valid number or not
            do{
                printf("\nEnter Number:");
                // To check if input is a valid integer and only one integer
                if(scanf("%d", &number) != 1){
                    printf("\nInvalid Input\n");
        
                    while(getchar() != '\n');
                    printf("\nDo you wanna try? (y/ n): ");
                    scanf("%c", &invalid);
                } else if(number <= 1){
                    printf("\nNot Prime\n");
                    printf("\nNumber must be >= 1");
            
                } else{
                    break; // break if the number is valid
                }
            } while(invalid == 'y' || invalid == 'Y'); //repeat until user enter's y
            if(invalid == 'n' || invalid == 'N'){
                break;
            }
            
            //checking function, to check weather the number is prime or not
            for(int i = 2; i <= sqrt(number); i++){
                if(number % i == 0){
                    prime = false;
                    printf("\nNOT prime\n");
                }
                break;
            }
            if(prime == true){
                printf("\nPRIME\n");
            }
            break;
        }
        
        //generating the prime number.
        while(choose == 'g' || choose == 'G'){
            do{
                printf("\nEnter number: ");
                if(scanf("%d", &number) != 1){
                    printf("\nInvalid input\n");
                    while(getchar() != '\n');
                    printf("\nDo you wanna try again? (y/ n): ");
                    scanf(" %c", &invalid);
                } else if(number <= 1){
                    printf("not prime\n");
                    printf("number must be >= 2\n");
                }else{
                    printf("\nReceived valid number: %d", number);
                    break;
                }
            } while(invalid == 'y' || invalid == 'Y');
            if(invalid == 'n' || invalid == 'N'){
                break;
            }

            //generating happens here
            printf("\nGenerating primes till %d: ", number);
            // iterate from 2 till number to check if it is prime
            for(int i = 2; i <= number; i++){
                // check if 'i' is prime
                is_prime = true;
                for(int d=2; d <= sqrt(i); d++){
                    if (i % d == 0) {
                        is_prime = false;
                        break;
                    }
                }
                // print 'i' if it is prime
                if (is_prime == true) {
                    printf("%d ", i);
                }
            }
            break;
        }
        printf("\nDo you wanna play? (y/ n): ");
        scanf(" %c", &again);
        if(again == 'n' || again == 'N'){
            printf("\n===================================\n");
            printf("      Thank you for playing");
            printf("\n===================================\n");
            break;
        }
        
    }while(again == 'y' || again == 'Y'); //restarting the game
    
}
