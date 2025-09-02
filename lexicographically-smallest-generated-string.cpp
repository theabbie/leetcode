class Solution {
public:
    string generateString(string check, string pat) {
        int L = check.size(), m = pat.size(), n = L + m - 1;
        vector<char> S(n, '*');
        vector<bool> forced(n, false);
        vector<int> unknown_count(L, m), mismatch_count(L, 0);
        for (int i = 0; i < L; i++) {
            if (check[i] == 'T') {
                for (int j = 0; j < m; j++) {
                    int pos = i + j;
                    if (S[pos] == '*') {
                        S[pos] = pat[j];
                        forced[pos] = true;
                        int start = max(0, pos - m + 1), end = min(pos, L - 1);
                        for (int w = start; w <= end; w++) {
                            unknown_count[w]--;
                            if (S[pos] != pat[pos - w])
                                mismatch_count[w]++;
                        }
                    } else if (S[pos] != pat[j])
                        return "";
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (S[i] == '*') {
                char cand = 0;
                int start = max(0, i - m + 1), end = min(i, L - 1);
                for (char c = 'a'; c <= 'z'; c++) {
                    bool valid = true;
                    for (int w = start; w <= end; w++) {
                        int new_unknown = unknown_count[w] - 1;
                        int new_mismatch = mismatch_count[w] + (c != pat[i - w] ? 1 : 0);
                        if (new_unknown == 0 && new_mismatch == 0) { valid = false; break; }
                    }
                    if (valid) { cand = c; break; }
                }
                if (!cand) return "";
                S[i] = cand;
                for (int w = start; w <= end; w++) {
                    unknown_count[w]--;
                    if (S[i] != pat[i - w])
                        mismatch_count[w]++;
                }
            }
        }
        for (int w = 0; w < L; w++) {
            if (check[w] == 'F' && unknown_count[w] == 0 && mismatch_count[w] == 0)
                return "";
        }
        return string(S.begin(), S.end());
    }
};