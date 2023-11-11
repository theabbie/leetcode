class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int res = 0;
        for (int i = 0; i < n; i++) {
            int j = i;
            HashSet<Character> seen = new HashSet<>();
            while (j < n && !seen.contains(s.charAt(j))) {
                seen.add(s.charAt(j));
                j++;
            }
            res = Math.max(res, j - i);
        }
        return res;
    }
}