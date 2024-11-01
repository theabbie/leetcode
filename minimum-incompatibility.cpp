class Solution {
public:
    int minimumIncompatibility(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<int> dp(1 << n, std::numeric_limits<int>::max());
        dp[0] = 0;
        std::vector<int> val(1 << n);
        std::vector<bool> good(1 << n, true);
        
        for (int mask = 1; mask < (1 << n); ++mask) {
            std::set<int> seen;
            int mn = std::numeric_limits<int>::max();
            int mx = std::numeric_limits<int>::min();
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    mn = std::min(mn, nums[i]);
                    mx = std::max(mx, nums[i]);
                    if (seen.count(nums[i]) > 0) {
                        good[mask] = false;
                    }
                    seen.insert(nums[i]);
                }
            }
            val[mask] = mx - mn;
        }
        
        for (int mask = 1; mask < (1 << n); ++mask) {
            int submask = mask;
            while (submask) {
                if (k * __builtin_popcount(submask) == n && good[submask] && dp[mask ^ submask] != std::numeric_limits<int>::max()) {
                    dp[mask] = std::min(dp[mask], val[submask] + dp[mask ^ submask]);
                }
                submask = (submask - 1) & mask;
            }
        }
        
        if (dp[(1 << n) - 1] == std::numeric_limits<int>::max()) {
            dp[(1 << n) - 1] = -1;
        }
        return dp[(1 << n) - 1];
    }
};