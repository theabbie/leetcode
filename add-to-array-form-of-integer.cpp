class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
        int digit;
        int carry = 0;
        int tmp;
        int i = 0;
        int n = A.size();
        int nd = K>0?floor(log10(K) + 1):1;
        while (i != max(n,nd)) {
            digit = K%10;
            if (i>=n) A.insert(A.begin(),0);
            n = A.size();
            tmp = A[n-i-1]+digit+carry;
            A[n-i-1] = tmp%10;
            carry = tmp/10;
            K = K/10;
            i++;
        }
        if (carry == 1) {
            A.insert(A.begin(),0);
            A[0] = carry;
        }
        return A;
    }
};