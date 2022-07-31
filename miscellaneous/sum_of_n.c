#include <stdio.h>

int sum(int n) {
    if (n == 0) {
        return 0;
    }
    return n + sum(n - 1);
}

void main() {
    int n;
    scanf("%d", &n);
    int res = sum(n);
    printf("%d", res);
}