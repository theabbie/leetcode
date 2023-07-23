#include <bits/stdc++.h>

using namespace std;

class TrieNode {
public:
    map<char, TrieNode*> child;
    bool end;
    int ctr;

    TrieNode() {
        end = false;
        ctr = 0;
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(const string& s) {
        TrieNode* curr = root;
        curr->ctr++;
        for (char c : s) {
            if (curr->child.find(c) == curr->child.end()) {
                curr->child[c] = new TrieNode();
            }
            curr = curr->child[c];
            curr->ctr++;
        }
        curr->end = true;
    }

    void erase(const string& s) {
        TrieNode* curr = root;
        curr->ctr--;
        for (char c : s) {
            curr = curr->child[c];
            curr->ctr--;
        }
        curr->end = false;
    }

    int countSmaller(const string& s) {
        TrieNode* curr = root;
        int res = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            bool done = true;
            for (auto it = curr->child.begin(); it != curr->child.end(); ++it) {
                char c = it->first;
                if (c < s[i]) {
                    res += it->second->ctr;
                }
                else if (c == s[i]) {
                    curr = it->second;
                    done = false;
                    break;
                }
            }
            if (done) {
                break;
            }
        }
        return res;
    }
};

string padstr(int x) {
    string str = to_string(x);
    if (str.length() < 10) {
        str = string(10 - str.length(), '0') + str;
    }
    return str;
}

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Trie trie;
    for (int el : arr) {
        trie.insert(padstr(el));
    }
    
    for (int i = 0; i < q; i++) {
        char t;
        int a, b;
        cin >> t >> a >> b;
        if (t == '!') {
            trie.erase(padstr(arr[a - 1]));
            arr[a - 1] = b;
            trie.insert(padstr(arr[a - 1]));
        }
        else {
            int count = trie.countSmaller(padstr(b + 1)) - trie.countSmaller(padstr(a));
            cout << count << "\n";
        }
    }

    return 0;
}