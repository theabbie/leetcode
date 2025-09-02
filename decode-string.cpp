class Solution {
public:
   string decodeString(string s) {
        int count = 0;
        string curr = "";
        stack<pair<int, string>> st;
        for (char c : s) {
            if (c == '[') {
                st.push({count, curr});
                count = 0;
                curr = "";
            }
            else if (c == ']') {
                pair<int, string> top = st.top();
                st.pop();
                string prev = top.second;
                int prevCount = top.first;
                curr = prev + repeat(curr, prevCount);
                
            }
            else if (isalpha(c)) {
                curr += c;
            }
            else {
                count = 10 * count + (c - '0');
            }
        }
        return curr;
    }
private:
    string repeat(string s, int k) {
        string result = "";
        for (int i = 0; i < k; ++i) {
            result += s;
        }
        return result;
    }
};