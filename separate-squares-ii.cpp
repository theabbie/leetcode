struct LazySegTree {
    int n;
    vector<int> cnt;
    vector<double> total;
    vector<double> xs;
    LazySegTree(const vector<double>& xs_) {
        xs = xs_;
        n = xs.size() - 1;
        cnt.assign(4 * n, 0);
        total.assign(4 * n, 0.0);
    }
    void update(int v, int tl, int tr, int l, int r, int h) {
        if(l > r) return;
        if(tl == l && tr == r) {
            cnt[v] += h;
        } else {
            int tm = (tl + tr) / 2;
            if(r <= tm) update(2 * v, tl, tm, l, r, h);
            else if(l > tm) update(2 * v + 1, tm + 1, tr, l, r, h);
            else {
                update(2 * v, tl, tm, l, tm, h);
                update(2 * v + 1, tm + 1, tr, tm + 1, r, h);
            }
        }
        if(cnt[v] > 0) total[v] = xs[tr + 1] - xs[tl];
        else if(tl == tr) total[v] = 0;
        else total[v] = total[2 * v] + total[2 * v + 1];
    }
};

struct Event {
    double y;
    int type;
    double x1, x2;
};

class Solution {
public:
    double rectangleArea(const vector<vector<double>>& rects) {
        if(rects.empty()) return 0;
        vector<double> xs;
        for(auto &r : rects) {
            xs.push_back(r[0]);
            xs.push_back(r[2]);
        }
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        if(xs.size() < 2) return 0;
        int n = xs.size() - 1;
        LazySegTree seg(xs);
        vector<Event> events;
        for(auto &r : rects) {
            events.push_back({r[1], 1, r[0], r[2]});
            events.push_back({r[3], -1, r[0], r[2]});
        }
        sort(events.begin(), events.end(), [](const Event &a, const Event &b){
            return a.y < b.y;
        });
        double cur_y = events[0].y, area = 0;
        for(auto &e : events) {
            area += (e.y - cur_y) * seg.total[1];
            cur_y = e.y;
            int l = lower_bound(xs.begin(), xs.end(), e.x1) - xs.begin();
            int r = lower_bound(xs.begin(), xs.end(), e.x2) - xs.begin() - 1;
            seg.update(1, 0, n - 1, l, r, e.type);
        }
        return area;
    }
    pair<vector<vector<double>>, vector<vector<double>>> split(const vector<vector<int>>& squares, double y) {
        vector<vector<double>> below, above;
        for(auto &sq : squares) {
            double x = sq[0], yi = sq[1], li = sq[2];
            if(yi + li <= y) {
                below.push_back({x, yi, x + li, yi + li});
            } else if(yi >= y) {
                above.push_back({x, yi, x + li, yi + li});
            } else {
                below.push_back({x, yi, x + li, y});
                above.push_back({x, y, x + li, yi + li});
            }
        }
        return {below, above};
    }
    double separateSquares(const vector<vector<int>>& squares) {
        vector<vector<double>> rects;
        double maxY = 0;
        for(auto &sq : squares) {
            double x = sq[0], y = sq[1], l = sq[2];
            rects.push_back({x, y, x + l, y + l});
            maxY = max(maxY, y + l);
        }
        if(rects.empty()) return 0;
        vector<double> xs;
        for(auto &r : rects) {
            xs.push_back(r[0]);
            xs.push_back(r[2]);
        }
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        vector<Event> events;
        for(auto &r : rects) {
            events.push_back({r[1], 1, r[0], r[2]});
            events.push_back({r[3], -1, r[0], r[2]});
        }
        sort(events.begin(), events.end(), [](const Event &a, const Event &b){
            return a.y < b.y;
        });
        LazySegTree seg(xs);
        double total_area = 0, cur_y = events[0].y;
        int i = 0;
        while(i < events.size()) {
            double y = events[i].y;
            total_area += (y - cur_y) * seg.total[1];
            cur_y = y;
            while(i < events.size() && events[i].y == y) {
                int l = lower_bound(xs.begin(), xs.end(), events[i].x1) - xs.begin();
                int r = lower_bound(xs.begin(), xs.end(), events[i].x2) - xs.begin() - 1;
                seg.update(1, 0, xs.size() - 2, l, r, events[i].type);
                i++;
            }
        }
        double half_area = total_area / 2;
        LazySegTree seg2(xs);
        double cum = 0;
        cur_y = events[0].y;
        i = 0;
        while(true) {
            double next_y = (i < events.size() ? events[i].y : maxY);
            double L = seg2.total[1];
            double dy = next_y - cur_y;
            if(cum + dy * L >= half_area) return cur_y + (half_area - cum) / L;
            cum += dy * L;
            cur_y = next_y;
            if(i < events.size()) {
                while(i < events.size() && events[i].y == cur_y) {
                    int l = lower_bound(xs.begin(), xs.end(), events[i].x1) - xs.begin();
                    int r = lower_bound(xs.begin(), xs.end(), events[i].x2) - xs.begin() - 1;
                    seg2.update(1, 0, xs.size() - 2, l, r, events[i].type);
                    i++;
                }
            } else break;
            if(cur_y >= maxY) break;
        }
        return maxY;
    }
};