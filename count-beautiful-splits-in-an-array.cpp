class Solution {
public:
    int beautifulSplits(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> lcp(n + 1, vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (nums[i] == nums[j]) {
                    lcp[i][j] = 1 + lcp[i + 1][j + 1];
                } else {
                    lcp[i][j] = 0;
                }
            }
        }

        int res = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (i > 0) {
                    if (min({lcp[0][i], i, j - i}) >= i ||
                        min({lcp[i][j], j - i, n - j}) >= j - i) {
                        ++res;
                    }
                }
            }
        }
        return res;
    }
};