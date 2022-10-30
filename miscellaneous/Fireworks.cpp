#include <iostream>

int sum(int n) {
    int s = 0;
    while (n) {
        s += n % 10;
        n = n / 10;
    }
    return s;
}

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        int n;
        std::cin >> n;
        int i = 1;
        int res = 0;
        while (i * i <= n) {
            if (n % i == 0) {
                if (i == sum(n / i)) res++;
            }
            i++;
        }
        std::cout << res << "\n";
    }
    return 0;
}