class Solution {
public:
    int deleteString(string s) {
        int n = s.length();
        vector<vector<int>> lcp(n, vector<int>(n, 0));
        vector<int> dp(n, 1);
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int curr = 1 + ((i + 1 < n && j + 1 < n) ? lcp[i + 1][j + 1] : 0);
                if (s[i] != s[j]) {
                    curr = 0;
                }
                lcp[i][j] = curr;
                if (i < j && lcp[i][j] >= j - i) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
        }
        
        return dp[0];
    }
};