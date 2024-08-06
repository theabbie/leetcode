class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        int n = jobs.size();
        vector<int> sums;
        for (int mask = 1; mask < (1 << n); mask++) {
            int sum = 0;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    sum += jobs[i];
                }
            }
            sums.push_back(sum);
        }
        
        vector<int> dp(1 << n, INT_MAX);
        dp[0] = 0;
        vector<int> ndp = dp;
        
        for (int rem = 1; rem <= k; rem++) {
            for (int mask = 0; mask < (1 << n); mask++) {
                int submask = mask;
                while (submask) {
                    ndp[mask] = min(ndp[mask], max(sums[submask - 1], dp[mask & ~submask]));
                    submask = (submask - 1) & mask;
                }
            }
            swap(dp, ndp);
        }
        
        return dp[(1 << n) - 1];
    }
};