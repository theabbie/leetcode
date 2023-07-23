#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<set<int>> graph(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u - 1].insert(v - 1);
        graph[v - 1].insert(u - 1);
    }
    graph[0].insert(-1);

    stack<pair<int, int>> stk;
    vector<int> indegree(n);
    stk.push({0, -1});

    while (!stk.empty()) {
        int curr = stk.top().first;
        int prev = stk.top().second;
        stk.pop();
        graph[curr].erase(prev);
        for (int j : graph[curr]) {
            stk.push({j, curr});
            indegree[j]++;
        }
    }

    deque<int> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push_front(i);
        }
    }

    vector<int> order;
    while (!q.empty()) {
        int curr = q.back();
        q.pop_back();
        order.push_back(curr);
        for (int j : graph[curr]) {
            indegree[j]--;
            if (indegree[j] == 0) {
                q.push_front(j);
            }
        }
    }
    reverse(order.begin(), order.end());

    vector<set<int>> subsets(n);
    vector<int> res(n);
    for (int i = 0; i < n; i++) {
        subsets[i].insert(arr[i]);
    }

    for (int curr : order) {
        for (int j : graph[curr]) {
            if (subsets[curr].size() < subsets[j].size()) {
                swap(subsets[curr], subsets[j]);
            }
            for (int el : subsets[j]) {
                subsets[curr].insert(el);
            }
        }
        res[curr] = subsets[curr].size();
    }

    for (int i = 0; i < n; i++) {
        cout << res[i] << " ";
    }
    cout << endl;

    return 0;
}
