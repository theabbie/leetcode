#include <stdio.h>

void func(int n) {
    n++;
    printf("Value Inside Pass By Value Function: %d\n", n);
}

void main() {
    int n;
    scanf("%d", &n);
    printf("Value Before Pass By Value: %d\n", n);
    func(n);
    printf("Value After Pass By Value: %d\n", n);
}