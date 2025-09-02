class Solution {
public:
    int gcd(int a, int b) {
        while (b) {
            int temp = a;
            a = b;
            b = temp % a;
        }
        return a;
    }

    bool isGoodArray(vector<int>& nums) {
        int g = 0;
        for (auto el : nums) g = gcd(g, el);
        return g == 1;
    }
};