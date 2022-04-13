class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> dup;
        int i = 0;
        int j = i;
        int longest = 0;
        int n = s.length();
        while (j < n) {
            if (dup.count(s[j]) == 0) {
                dup[s[j]] = j;
                j += 1;
                longest = max(longest, j - i);
            }
            else {
                i = dup[s[j]] + 1;
                j = i;
                dup.clear();
            }
        }
        return longest;
    }
};