#include <iostream>
#include <set>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> waiting(n);
    for (int i = 0; i < n; i++) {
        waiting[i] = i + 1;
    }

    set<int> called;
    vector<int> res;
    for (int i = 0; i < q; i++) {
        int op;
        cin >> op;
        if (op == 1) {
            called.insert(waiting[0]);
            waiting.erase(waiting.begin());
        } else if (op == 2) {
            int x;
            cin >> x;
            auto it = called.lower_bound(x);
            if (it != called.end() && *it == x) {
                called.erase(it);
            }
        } else {
            if (!called.empty()) {
                res.push_back(*called.begin());
            }
        }
    }

    for (int i = 0; i < (int)res.size(); i++) {
        cout << res[i] << endl;
    }

    return 0;
}
