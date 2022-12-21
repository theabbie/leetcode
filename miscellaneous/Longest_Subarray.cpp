#include <iostream>

bool possible(int arr[], int ctr[32], int n, int k)
{
    int curr[32];
    for (int b = 0; b < 32; b++)
        curr[b] = 0;
    for (int i = 0; i < n; i++)
    {
        for (int b = 0; b < 32; b++)
        {
            if (arr[i] & (1 << b))
                curr[b] += 1;
        }
        if (i >= k)
        {
            for (int b = 0; b < 32; b++)
            {
                if (arr[i - k] & (1 << b))
                    curr[b] -= 1;
            }
        }
        if (i >= k - 1)
        {
            bool found = true;
            for (int b = 0; b < 32; b++)
            {
                if ((curr[b] > 0) ^ (ctr[b] - curr[b] > 0))
                {
                    found = false;
                    break;
                }
            }
            if (found)
                return true;
        }
    }
    return false;
}

int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        int n;
        std::cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            std::cin >> arr[i];
        int ctr[32];
        for (int b = 0; b < 32; b++)
            ctr[b] = 0;
        for (int i = 0; i < n; i++)
        {
            for (int b = 0; b < 32; b++)
            {
                if (arr[i] & (1 << b))
                    ctr[b] += 1;
            }
        }
        int beg = 1;
        int end = n;
        int res = -1;
        while (beg <= end)
        {
            int mid = (beg + end) / 2;
            if (possible(arr, ctr, n, mid))
            {
                res = mid;
                beg = mid + 1;
            }
            else
            {
                end = mid - 1;
            }
        }
        std::cout << res << '\n';
    }
    return 0;
}