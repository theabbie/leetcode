class Solution {
public:
    long long minimumCost(vector<int>& nums, vector<int>& cost, int k) {
        int n = nums.size();
        vector<long long> p(n + 1, 0), cp(n + 1, 0);
        for (int i = 0; i < n; i++) {
            p[i + 1] = p[i] + nums[i];
            cp[i + 1] = cp[i] + cost[i];
        }
        const long long INF = 1LL << 60;
        vector<long long> dp(n + 1, INF), ndp(n + 1, INF);
        struct Frame {
            int L, R, optL, optR;
        };
        for (int ps = n; ps >= 1; ps--) {
            dp[n] = 0;
            vector<Frame> stack;
            stack.push_back({0, n - 1, 0, n - 1});
            while (!stack.empty()) {
                Frame cur = stack.back();
                stack.pop_back();
                int L = cur.L, R = cur.R, optL = cur.optL, optR = cur.optR;
                if (L > R) continue;
                int mid = (L + R) / 2;
                long long best = INF;
                int opt = optL;
                int rbound = min(optR, n - 1);
                for (int j = optL; j <= rbound; j++) {
                    long long cand;
                    if (dp[j + 1] == INF)
                        cand = INF;
                    else {
                        long long part = p[j + 1] + k * (long long)ps;
                        long long delta = cp[j + 1] - cp[mid];
                        if (part > 0 && delta > 0 && part > INF / delta)
                            cand = INF;
                        else
                            cand = part * delta + dp[j + 1];
                    }
                    if (cand < best) {
                        best = cand;
                        opt = j;
                    }
                }
                ndp[mid] = best;
                stack.push_back({mid + 1, R, opt, optR});
                stack.push_back({L, mid - 1, optL, opt});
            }
            dp.swap(ndp);
            fill(ndp.begin(), ndp.end(), INF);
        }
        return dp[0];
    }
};