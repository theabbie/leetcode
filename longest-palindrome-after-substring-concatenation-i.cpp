class Solution {
public:
    int longestPalindrome(string s, string t) {
        int m = s.size(), n = t.size(), ans = 0;
        vector<vector<bool>> dpS(m, vector<bool>(m, false));
        vector<int> leftS(m, 0);
        for (int i = m - 1; i >= 0; i--) {
            for (int j = i; j < m; j++) {
                if (s[i] == s[j] && (j - i < 2 || dpS[i+1][j-1])) {
                    dpS[i][j] = true;
                    leftS[i] = max(leftS[i], j - i + 1);
                    ans = max(ans, leftS[i]);
                }
            }
        }
        vector<vector<bool>> dpT(n, vector<bool>(n, false));
        vector<int> rightT(n, 0);
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (t[i] == t[j] && (j - i < 2 || dpT[i+1][j-1])) {
                    dpT[i][j] = true;
                    rightT[j] = max(rightT[j], j - i + 1);
                    ans = max(ans, rightT[j]);
                }
            }
        }
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = n - 1; j >= 0; j--) {
                if (s[i] == t[j]) {
                    dp[i][j] = 1;
                    if(i > 0 && j < n - 1) dp[i][j] += dp[i-1][j+1];
                }
                if(dp[i][j]){
                    int extra = 0;
                    if(i + 1 < m) extra = max(extra, leftS[i+1]);
                    if(j - 1 >= 0) extra = max(extra, rightT[j-1]);
                    ans = max(ans, 2 * dp[i][j] + extra);
                }
            }
        }
        return ans;
    }
};