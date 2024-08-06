#include <bitset>
#include <vector>

class Solution {
public:
    Solution() {
        f.resize(1001, std::bitset<1001>(0));
        calculateF();
    }

    int distinctPrimeFactors(std::vector<int>& nums) {
        std::bitset<1001> res;
        for (const auto& el : nums) {
            res |= f[el];
        }
        return res.count();
    }

private:
    std::vector<std::bitset<1001>> f;

    void calculateF() {
        std::bitset<1001> mask(2);

        for (int i = 2; i <= 1000; ++i) {
            mask <<= 1;
            int j = 1;
            if (f[i].any()) {
                continue;
            }
            while (i * j <= 1000) {
                f[i * j] |= mask;
                j += 1;
            }
        }
    }
};