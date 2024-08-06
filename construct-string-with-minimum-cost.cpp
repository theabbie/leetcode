#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <climits>

using namespace std;

vector<int> computeLPS(const string& pattern) {
    int length = 0;
    vector<int> lps(pattern.size(), 0);
    int i = 1;
    while (i < pattern.size()) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

vector<int> findPatternIndices(const string& text, const string& pattern) {
    vector<int> indices;
    int n = text.size();
    int m = pattern.size();
    vector<int> lps = computeLPS(pattern);
    int i = 0, j = 0;
    while (i < n) {
        if (text[i] == pattern[j]) {
            i++;
            j++;
            if (j == m) {
                indices.push_back(i - j);
                j = lps[j - 1];
            }
        } else {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return indices;
}

class TrieNode {
public:
    unordered_map<char, TrieNode*> child;
    int cost;
    
    TrieNode() : cost(INT_MAX) {}
};

class Trie {
public:
    TrieNode* root;
    
    Trie() {
        root = new TrieNode();
    }
    
    void insert(const string& s, int cost) {
        TrieNode* curr = root;
        for (char c : s) {
            if (curr->child.find(c) == curr->child.end()) {
                curr->child[c] = new TrieNode();
            }
            curr = curr->child[c];
        }
        curr->cost = min(curr->cost, cost);
    }
};

class Solution {
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        int n = target.size();
        vector<int> dp(n + 1, INT_MAX);
        dp[n] = 0;

        vector<pair<string, int>> vals;
        for (int i = 0; i < words.size(); ++i) {
            vals.emplace_back(words[i], costs[i]);
        }
        sort(vals.begin(), vals.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
            return a.first.size() > b.first.size();
        });

        int K = 0;
        for (const string& w : words) {
            K += w.size();
        }

        vector<vector<pair<int, int>>> mincosts(n);
        Trie trie;

        for (const auto& [w, c] : vals) {
            int l = w.size();
            if (l * l <= K) {
                trie.insert(w, c);
                continue;
            }
            for (int i : findPatternIndices(target, w)) {
                mincosts[i].emplace_back(l, c);
            }
        }

        for (int i = n - 1; i >= 0; --i) {
            int j = i;
            TrieNode* root = trie.root;
            while (j < n && root->child.find(target[j]) != root->child.end()) {
                root = root->child[target[j]];
                if (root->cost != INT_MAX && dp[j + 1] != INT_MAX) dp[i] = min(dp[i], root->cost + dp[j + 1]);
                int l = j - i + 1;
                if (l * l > K) {
                    break;
                }
                j++;
            }
            for (const auto& [l, c] : mincosts[i]) {
                if (dp[i + l] != INT_MAX) dp[i] = min(dp[i], c + dp[i + l]);
            }
        }

        return dp[0] == INT_MAX ? -1 : dp[0];
    }
};