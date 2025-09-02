class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        double cx = side / 2.0, cy = side / 2.0;
        sort(points.begin(), points.end(), [&](const vector<int>& a, const vector<int>& b) {
            return atan2(a[1] - cy, a[0] - cx) > atan2(b[1] - cy, b[0] - cx);
        });
        auto md = [&](int i, int j) -> int {
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
        };
        auto get_next = [&](int i, int mid) -> int {
            int base = i % n;
            int lo = i + 1, hi = i + n - 1;
            while (lo < hi) {
                int m = (lo + hi + 1) / 2;
                int d1 = abs(points[base][0] - points[((m - 1) % n)][0]) + abs(points[base][1] - points[((m - 1) % n)][1]);
                int d2 = abs(points[base][0] - points[(m % n)][0]) + abs(points[base][1] - points[(m % n)][1]);
                if (d1 < d2)
                    lo = m;
                else
                    hi = m - 1;
            }
            int peak = lo;
            int candidate1 = -1;
            int lo1 = i + 1, hi1 = peak;
            while (lo1 <= hi1) {
                int m = (lo1 + hi1) / 2;
                int d = abs(points[base][0] - points[(m % n)][0]) + abs(points[base][1] - points[(m % n)][1]);
                if (d >= mid) { candidate1 = m; hi1 = m - 1; }
                else lo1 = m + 1;
            }
            int candidate2 = -1;
            int lo2 = peak, hi2 = i + n - 1;
            while (lo2 <= hi2) {
                int m = (lo2 + hi2) / 2;
                int d = abs(points[base][0] - points[(m % n)][0]) + abs(points[base][1] - points[(m % n)][1]);
                if (d >= mid) { candidate2 = m; hi2 = m - 1; }
                else lo2 = m + 1;
            }
            if (candidate1 == -1 && candidate2 == -1)
                return -1;
            if (candidate1 == -1)
                return candidate2;
            if (candidate2 == -1)
                return candidate1;
            return candidate1 < candidate2 ? candidate1 : candidate2;
        };
        auto can = [&](int mid) -> bool {
            for (int i = 0; i < n; i++) {
                int cnt = 1, cur = i;
                bool valid = true;
                while (cnt < k) {
                    int nxt = get_next(cur, mid);
                    if (nxt == -1 || nxt >= i + n) { valid = false; break; }
                    cur = nxt;
                    cnt++;
                }
                if (valid && cnt == k && md(cur % n, i % n) >= mid)
                    return true;
            }
            return false;
        };
        long long lo_val = 0, hi_val = 2LL * side, ans = 0;
        while (lo_val <= hi_val) {
            long long mid = (lo_val + hi_val) / 2;
            if (can((int)mid)) { ans = mid; lo_val = mid + 1; }
            else { hi_val = mid - 1; }
        }
        return (int)ans;
    }
};