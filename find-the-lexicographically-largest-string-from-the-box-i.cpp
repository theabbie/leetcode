class Solution {
public:
    string answerString(string word, int numFriends) {
        int n = word.size();
        if (numFriends == 1) {
            return word;
        }
        string largest_substr = "";
        int mx = n - (numFriends - 1);
        for (int l = 1; l <= mx; ++l) {
            largest_substr = max(largest_substr, word.substr(0, l));
            largest_substr = max(largest_substr, word.substr(n - l, l));
        }
        if (numFriends == 2) {
            return largest_substr;
        }
        largest_substr = max(largest_substr, word.substr(0, mx));
        for (int i = 1; i <= n - mx; ++i) {
            largest_substr = max(largest_substr, word.substr(i, mx));
        }
        return largest_substr;
    }
};