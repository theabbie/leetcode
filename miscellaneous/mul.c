#include <stdio.h>
#include <time.h>

int square(int n) {
    int k;
    if (n == 0 || n == 1) return n;
    if (n & 1) {
        k = (n - 1) >> 1;
        return (square(k) << 2) + (k << 2) + 1;
    }
    k = n >> 1;
    return square(k) << 2;
}

int mul(int a, int b) {
    if (a > b) return mul(b, a);
    int k = b - a;
    if (k & 1) return mul(a, b + 1) - a;
    k = k >> 1;
    return square(a + k) - square(k);
}

int main() {
    int a, b;
    clock_t t;
    scanf("%d %d", &a, &b);

    t = clock();
    printf("\n%d\n", mul(a, b));
    t = clock() - t;
    printf("%f\n", 100000 * (float)t / CLOCKS_PER_SEC);

    t = clock();
    printf("\n%d\n", a * b);
    t = clock() - t;
    printf("%f\n", 100000 * (float)t / CLOCKS_PER_SEC);
}