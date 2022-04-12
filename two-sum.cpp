class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            if (seen.count(target - nums[i]) != 0) {
                return {seen[target - nums[i]], i};
            }
            else {
                seen[nums[i]] = i;
            }
        }
        return {0, 0};
    }
};