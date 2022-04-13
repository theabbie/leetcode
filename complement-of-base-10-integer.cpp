class Solution {
public:
    int bitwiseComplement(int N) {
        int digit;
        int comp = 0;
        int i = 0;
        if (N == 0) return 1;
        while (N != 0) {
            digit = N%2;
            N = N/2;
            comp += (1-digit)*pow(2,i);
            i++;
        }
        return comp;
    }
};