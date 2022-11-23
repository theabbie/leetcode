#include <bits/stdc++.h>
using namespace std;
long long int productPrimeFactors(int n)
{
	long long int product = 1;
	if (n % 2 == 0) {
		product *= 2;
		while (n % 2 == 0)
			n = n / 2;
	}
	for (int i = 3; i <= sqrt(n); i = i + 2) {
		if (n % i == 0) {
			product = product * i;
			while (n % i == 0)
				n = n / i;
		}
	}
	if (n > 2)
		product = product * n;

	return product;
}

long long int gcd(long long int a, long long int b) {
    while (b) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main()
{
	int t;
    cin >> t;
    while (t--) {
        long long int a, b;
        cin >> a >> b;
        a = productPrimeFactors(a);
        b = productPrimeFactors(b);
        int g = gcd(a, b);
        if (a % (b / g) == 0) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
	return 0;
}
