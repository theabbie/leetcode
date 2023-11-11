class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        HashMap<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (pos.containsKey(target - nums[i])) {
                return new int[]{pos.get(target - nums[i]), i};
            }
            pos.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }
}