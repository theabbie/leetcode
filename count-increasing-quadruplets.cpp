class BIT{
public:
    vector<int> a;
    int N;
    BIT(int n){
        a.resize(n + 1);
        N = n;
    }
    
    void update(int ind,int val){
        while(ind <= N){
            a[ind] += val;
            ind += ind & (-ind);
        }
    }
    
    long long query(int ind){
        long long sum = 0;
        while(ind > 0){
            sum += a[ind];
            ind -= ind & (-ind);
        }
        return sum;
    }
};

class Solution {
public:
    long long int countQuadruplets(vector<int>& nums) {
        int n = nums.size();
        int M = *max_element(nums.begin(), nums.end());
        long long int res = 0;
        BIT left(M + 1);
        for (int i = 0; i < n; i++) {
            BIT right(M + 1);
            for (int j = n - 1; j > i; j--) {
                if (nums[i] > nums[j]) {
                    int l = left.query(nums[j]);
                    int r = right.query(M + 1) - right.query(nums[i]);
                    res += l * r;
                }
                right.update(nums[j], 1);
            }
            left.update(nums[i], 1);
        }
        return res;
    }
};