#include <vector>
#include <algorithm>
using namespace std;

const int M = 1000000007;
const int MAXN = 100001;
vector<int> fact(MAXN), invFact(MAXN);
bool precomputed = false;

int modExp(int base, int exp, int mod) {
    int result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (1LL * result * base) % mod;
        }
        base = (1LL * base * base) % mod;
        exp /= 2;
    }
    return result;
}

void precomputeFactorials() {
    fact[0] = 1;
    for (int i = 1; i < MAXN; ++i) {
        fact[i] = (1LL * fact[i - 1] * i) % M;
    }
    invFact[MAXN - 1] = modExp(fact[MAXN - 1], M - 2, M);
    for (int i = MAXN - 2; i >= 0; --i) {
        invFact[i] = (1LL * (i + 1) * invFact[i + 1]) % M;
    }
}

int comb(int n, int k) {
    if (k > n || k < 0) return 0;
    return (1LL * fact[n] * invFact[k] % M * invFact[n - k] % M) % M;
}

class Solution {
public:
    int minMaxSums(vector<int>& nums, int k) {
        if (!precomputed) {
            precomputeFactorials();
            precomputed = true;
        }
        int n = nums.size();
        sort(nums.begin(), nums.end());
        long long res = 0;
        for (int i = 0; i < n; ++i) {
            long long leftSum = 0, rightSum = 0;
            for (int x = 0; x < k; ++x) {
                leftSum = (leftSum + comb(i, x)) % M;
                rightSum = (rightSum + comb(n - i - 1, x)) % M;
            }
            res = (res + nums[i] * (leftSum + rightSum) % M) % M;
        }
        return res;
    }
};