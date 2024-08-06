class Solution {
public:
    int diameter(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<set<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }
        vector<int> sizes(n, 0);
        auto dfs = [&](auto&& dfs, int i, int prev) -> int {
            sizes[i] = 1;
            for (int j : graph[i]) {
                if (j != prev) {
                    sizes[i] += dfs(dfs, j, i);
                }
            }
            return sizes[i];
        };
        auto getcentroid = [&](auto&& getcentroid, int i, int prev, int total) -> int {
            for (int j : graph[i]) {
                if (j != prev && sizes[j] > total / 2) {
                    return getcentroid(getcentroid, j, i, total);
                }
            }
            return i;
        };
        auto longest = [&](auto&& longest, int i, int prev) -> int {
            int res = 1;
            for (int j : graph[i]) {
                if (j != prev) {
                    res = max(res, 1 + longest(longest, j, i));
                }
            }
            return res;
        };
        auto solve = [&](auto&& solve, int i) -> int {
            int total = dfs(dfs, i, -1);
            int centroid = getcentroid(getcentroid, i, -1, total);
            int a = 0, b = 0;
            for (int j : graph[centroid]) {
                int longest_val = longest(longest, j, centroid);
                if (longest_val > a) {
                    b = a;
                    a = longest_val;
                } else if (longest_val > b) {
                    b = longest_val;
                }
            }
            int res = a + b;
            for (int j : graph[centroid]) {
                graph[j].erase(centroid);
                res = max(res, solve(solve, j));
            }
            return res;
        };
        return solve(solve, 0);
    }

    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int a = diameter(edges1);
        int b = diameter(edges2);
        return max({a, b, (a + 1) / 2 + (b + 1) / 2 + 1});
    }
};