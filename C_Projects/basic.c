#include <stdio.h>

void sum(int a, int b);
void  multiply(int a, int b);
void  divide(int a, int b);
void remd(int a, int b);

int main(){
    sum(5, 2);
    multiply(5, 2);
    divide(5, 2);
    remd(5, 2);
    return 0;
}

void sum(int a, int b){
    int add = a + b;
    printf("your answer :\t %d\n", add);
}

void multiply(int a, int b){
    int multiply = a * b;
    printf("your answer :\t %d\n", multiply); 
}

void divide(int a, int b){
    float divide = a/b;
    printf("your answer :\t%f\n", divide);
}

void remd(int a, int b){
    int rem = a % b;
    printf("your answer :\t%d\n", rem);
}