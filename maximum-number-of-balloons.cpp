class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int k = 0;
        string mystr = "balloon";
        int N = mystr.length();
        bool flag;
        while (true) {
            flag = true;
            for (int i = 0; i < N; i++) {
                if (text.find(mystr.at(i)) != string::npos) text[text.find(mystr.at(i))]='x';
                else {
                    flag = false;
                    break;
                }
            }
            if (flag) k++;
            else break;
        }
        return k;
    }
};