int gcdMemo[1001][1001];

int memoizedGCD(int a, int b) {
    if (a == 0) return b;
    if (b == 0) return a;
    if (gcdMemo[a][b] != -1) return gcdMemo[a][b];
    return gcdMemo[a][b] = memoizedGCD(b, a % b);
}

pair<int, int> f(int x, int y) {
    int g = memoizedGCD(x, y);
    return {x / g, y / g};
}

class Solution {
public:
    Solution() {
        memset(gcdMemo, -1, sizeof(gcdMemo));
    }
    
    long long numberOfSubsequences(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        int maxVal = *max_element(nums.begin(), nums.end());

        vector<vector<int>> ctr(maxVal + 1, vector<int>(maxVal + 1, 0));

        long long res = 0;
        int q = 0;

        for (int r = 0; r < n; ++r) {
            while (q + 1 < r) {
                for (int p = 0; p < q - 1; ++p) {
                    auto key = f(nums[p], nums[q]);
                    ctr[key.first][key.second]++;
                }
                ++q;
            }

            for (int s = r + 2; s < n; ++s) {
                auto key = f(nums[s], nums[r]);
                res += ctr[key.first][key.second];
            }
        }

        return res;
    }
};