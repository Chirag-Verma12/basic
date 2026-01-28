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
    printf("\nWelcome\n");

    do{
        //choosing here to generate or checking
        printf("\nWhat do you wanna do, Generate or Check? (g/ c):");
        scanf(" %c", &choose); 

        //checking, prime or not
        while(choose == 'c'){
            prime = true;

            //checking if the user entered a valid number or not
            do{
                printf("\nEnter Number:");
                if(scanf("%d", &number) != 1){
                    printf("\nInvalid Input\n");
        
                while(getchar() != '\n');
                printf("\nDo you wanna try? (y/ n)");
                scanf(" %c", &invalid);
                } else if(number <= 1){
                    printf("\nNot Prime\n");
                    printf("\nNumber must be >= 1");
                    printf("\nWanna try again? (y/n): ");
                    scanf(" %c", &invalid);
            
                } else{
                    break; // break if the number is valid
                }
            } while(invalid == 'y' || invalid == 'Y'); //repeat until user enter's y

            if(invalid == 'n' || invalid == 'N'){ //breaking system, if user enter n in invalid it will stop
                printf("\nThanks\n");
                break;
            }
            //checking function, to check weather the number is prime or not
            for(int i = 2; i <= sqrt(number); i++){
                if(number % i == 0){
                    prime = false;
                    printf("\nNOT prime\n");
                    break;
                } 

            if(prime == true){
                printf("\nPRIME\n");
                break;
            }else{
                printf("\nWrong input\n");
            }
            }
            if(prime == true || prime == false){
                printf("\nDo you wanna try again? (y/ n)");
                scanf(" %c", &again);
                if(again == 'n' || again == 'N'){
                    printf("\nThank you for playing\n");
                    break;
                }
            }
        }
    } while(again == 'y' || again == 'Y'); //restarting the game
}

//Objective: 1. make the whole loop repeat, 2. in checker number 2 to 3 is not working