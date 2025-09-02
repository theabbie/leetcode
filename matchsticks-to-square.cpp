class Solution {
    bool check(vector<int> &sides,const vector<int> &matches, int index, int target) {
        if (index == matches.size())
            return sides[0] == sides[1] && sides[0] == sides[2] && sides[0] == sides[3];
        for (int i = 0; i < 4; ++i) {
            if (sides[i] + matches[index] > target) continue;
            sides[i] += matches[index];
            if (check(sides, matches, index + 1, target))
                return true;
            sides[i] -= matches[index];
        }
        return false;
    }
public:
    bool makesquare(vector<int>& nums) {
        if (nums.empty()) return false;
        int s = 0;
        for (int el : nums) s += el;
        if (s % 4 != 0) return false;
        int target = s / 4;
        sort(nums.begin(), nums.end(), greater<>());
        vector<int> sides(4, 0);
        return check(sides, nums, 0, target);
    }
};