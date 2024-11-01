class Solution {
public:
    int possibleStringCount(string word, int k) {
        const int M = 1e9 + 7;
        int n = word.size();
        long long res = 1;
        vector<int> w;
        int i = 0;
        while (i < n) {
            int ctr = 1;
            while (i < n - 1 && word[i] == word[i + 1]) {
                i++;
                ctr++;
            }
            res = (res * ctr) % M;
            w.push_back(ctr);
            i++;
        }
        std::vector<long long> dp(k, 1), ndp(k);
        for (int i = std::min(static_cast<int>(w.size()), k + 2) - 1; i >= 0; i--) {
            std::vector<long long> pf(k + 1, 0);
            for (int j = 0; j < k; j++) {
                pf[j + 1] = (pf[j] + dp[j]) % M;
            }
            for (int rem = 0; rem < k; rem++) {
                int x = std::min(w[i], rem);
                ndp[rem] = (pf[rem] - pf[rem - x] + M) % M;
            }
            dp = ndp;
        }
        res = (res - dp[k - 1] + M) % M;
        return static_cast<int>(res);
    }
};
