#include <vector>
#include <deque>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxMoves(int kx, int ky, vector<vector<int>>& positions) {
        static vector<vector<int>> dist(2500, vector<int>(2500, 0));
        static vector<bool> done(2500, false);
        int m = 50, n = 50;
        positions.push_back({kx, ky});
        for (auto el : positions) {
            int i = el[0];
            int j = el[1];
            int source = n * i + j;
            if (done[source]) continue;
            deque<tuple<int, int, int>> q;
            q.emplace_back(i, j, 0);
            vector<vector<bool>> v(m, vector<bool>(n, false));
            v[i][j] = true;

            while (!q.empty()) {
                auto [ii, jj, d] = q.back(); q.pop_back();
                dist[source][n * ii + jj] = d;

                for (int dx : {-2, -1, 1, 2}) {
                    for (int dy : {-2, -1, 1, 2}) {
                        if (abs(dx) == abs(dy)) continue;
                        int x = ii + dx, y = jj + dy;
                        if (x >= 0 && x < m && y >= 0 && y < n && !v[x][y]) {
                            v[x][y] = true;
                            q.emplace_front(x, y, d + 1);
                        }
                    }
                }
            }
            
            done[source] = true;
        }

        int n_positions = positions.size();
        int target = (1 << n_positions) - 1;
        vector<vector<vector<int>>> dp(n_positions, vector<vector<int>>(1 << n_positions, vector<int>(2, -1)));
        for (int i = 0; i < n_positions; ++i) dp[i][target][0] = dp[i][target][1] = 0;
        for (int mask = target - 1; mask >= 0; --mask) {
            for (int curr = 0; curr < n_positions; ++curr) {
                for (int alice = 0; alice < 2; ++alice) {
                    dp[curr][mask][alice] = alice ? -1e7 : 1e7;
                    for (int i = 0; i < n_positions - 1; ++i) {
                        if (!(mask & (1 << i))) {
                            int cost = dist[n * positions[curr][0] + positions[curr][1]][n * positions[i][0] + positions[i][1]];
                            if (alice) {
                                dp[curr][mask][alice] = max(dp[curr][mask][alice], cost + dp[i][mask | (1 << i)][1 - alice]);
                            } else {
                                dp[curr][mask][alice] = min(dp[curr][mask][alice], cost + dp[i][mask | (1 << i)][1 - alice]);
                            }
                        }
                    }
                }
            }
        }
        return dp[n_positions - 1][1 << (n_positions - 1)][1];
    }
};
