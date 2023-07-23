class Solution {
public:
    int mincost(std::vector<std::pair<int, int>>& vals, int n, int totsum) {
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(totsum + 1, 1000000000));
        
        for (int i = n; i >= 0; i--) {
            for (int curr = totsum; curr >= 0; curr--) {
                if (curr >= n) {
                    dp[i][curr] = 0;
                } else if (i < n) {
                    int a = vals[i].second + dp[i + 1][curr + vals[i].first];
                    int b = dp[i + 1][curr];
                    dp[i][curr] = std::min(a, b);
                }
            }
        }
        
        return dp[0][0];
    }
    
    int paintWalls(std::vector<int>& cost, std::vector<int>& time) {
        int n = cost.size();
        std::vector<std::pair<int, int>> vals;
        int totsum = 0;
        for (int i = 0; i < n; i++) {
            vals.push_back(std::make_pair(time[i] + 1, cost[i]));
            totsum += time[i] + 1;
        }
        return mincost(vals, n, totsum);
    }
};