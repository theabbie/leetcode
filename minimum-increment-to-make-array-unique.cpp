class Solution {
public:
    int minIncrementForUnique(std::vector<int>& nums) {
        int n = nums.size();
        int res = 0;

        std::sort(nums.begin(), nums.end());

        std::multiset<int> absent;
        for (int i = nums[0]; i < nums[n - 1] + n; i++) {
            absent.insert(i);
        }

        for (int i = 0; i < n; i++) {
            auto it = absent.lower_bound(nums[i]);
            int currNum = *it;
            res += currNum - nums[i];
            absent.erase(it);
        }

        return res;
    }
};