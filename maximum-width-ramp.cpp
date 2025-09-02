class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int n = nums.size();
        vector<int> mins;
        vector<int> maxes;
        int mv = 1e9;
        for (int i = 0; i < n; i++) {
            if (nums[i] < mv) mins.push_back(i);
            mv = min(mv, nums[i]);
        }
        mv = -1e9;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > mv) maxes.push_back(i);
            mv = max(mv, nums[i]);
        }
        int res = 0;
        for (int i : maxes) {
            while (mins.size() > 1 && nums[mins[mins.size() - 2]] <= nums[i]) {
                mins.pop_back();
            }
            if (mins.size() > 0 && nums[mins[mins.size() - 1]] <= nums[i]) {
                res = max(res, i - mins[mins.size() - 1]);
            }
        }
        return res;
    }
};