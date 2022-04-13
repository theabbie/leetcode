class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum = 0;
        int n = arr.size();
        for (int i = 1; i < n+1; i+=2) {
            for (int j = 0; j < n-i+1; j++) {
                for (int k = j; k < j+i; k++) {
                    sum += arr[k];
                }
            }
        }
        return sum;
    }
};