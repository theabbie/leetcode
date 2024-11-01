#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int countOfSubstrings(std::string word, int k) {
        int n = word.size();
        std::vector<int> p(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            p[i + 1] = p[i] + (word[i] != 'a' && word[i] != 'e' && word[i] != 'i' && word[i] != 'o' && word[i] != 'u');
        }

        auto count = [&](int x) {
            int res = 0;
            std::vector<int> last(5, n);

            for (int i = n - 1; i >= 0; --i) {
                if (word[i] == 'a') last[0] = i;
                else if (word[i] == 'e') last[1] = i;
                else if (word[i] == 'i') last[2] = i;
                else if (word[i] == 'o') last[3] = i;
                else if (word[i] == 'u') last[4] = i;

                int beg = i;
                int end = n - 1;

                while (beg <= end) {
                    int mid = (beg + end) / 2;
                    if (p[mid + 1] - p[i] >= x) {
                        end = mid - 1;
                    } else {
                        beg = mid + 1;
                    }
                }
                res += n - std::max(*std::max_element(last.begin(), last.end()), end + 1);
            }
            return res;
        };

        return count(k) - count(k + 1);
    }
};
