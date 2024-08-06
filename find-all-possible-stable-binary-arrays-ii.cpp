#include <vector>

const int M = 1000000007;

class FenwickTree {
private:
    std::vector<long long> bit;

public:
    FenwickTree(const std::vector<long long>& x) {
        bit = x;
        for (int i = 0; i < bit.size(); ++i) {
            int j = i | (i + 1);
            if (j < bit.size()) {
                bit[j] += bit[i];
                bit[j] %= M;
            }
        }
    }

    void update(int idx, long long x) {
        while (idx < bit.size()) {
            bit[idx] += x;
            bit[idx] %= M;
            idx |= idx + 1;
        }
    }

    long long query(int end) {
        long long x = 0;
        while (end) {
            x += bit[end - 1];
            x %= M;
            end &= end - 1;
        }
        return x;
    }
};

class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        std::vector<std::vector<std::vector<long long>>> dp(zero + 1, std::vector<std::vector<long long>>(one + 1, std::vector<long long>(2)));
        dp[0][0][0] = dp[0][0][1] = 1;

        std::vector<FenwickTree> rowsz(zero + 1, FenwickTree(std::vector<long long>(one + 1, 0)));
        std::vector<FenwickTree> rowso(zero + 1, FenwickTree(std::vector<long long>(one + 1, 0)));
        std::vector<FenwickTree> colsz(one + 1, FenwickTree(std::vector<long long>(zero + 1, 0)));
        std::vector<FenwickTree> colso(one + 1, FenwickTree(std::vector<long long>(zero + 1, 0)));
        rowsz[0].update(0, 1);
        colsz[0].update(0, 1);
        rowso[0].update(0, 1);
        colso[0].update(0, 1);

        for (int i = 0; i <= zero; ++i) {
            for (int j = 0; j <= one; ++j) {
                if (i == 0 && j == 0) continue;

                long long addz = colso[j].query(i) - colso[j].query(std::max(i - limit, 0));
                long long addo = rowsz[i].query(j) - rowsz[i].query(std::max(j - limit, 0));

                dp[i][j][0] = (dp[i][j][0] + addz + M) % M;
                dp[i][j][1] = (dp[i][j][1] + addo + M) % M;

                rowsz[i].update(j, addz);
                rowso[i].update(j, addo);
                colsz[j].update(i, addz);
                colso[j].update(i, addo);
            }
        }

        return (dp[zero][one][0] + dp[zero][one][1]) % M;
    }
};