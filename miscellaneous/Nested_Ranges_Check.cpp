#include <bits/stdc++.h>

struct Range {
    int start;
    int end;
    int index;
};

int main() {
    int n;
    std::cin >> n;

    std::vector<Range> ranges;

    for (int i = 0; i < n; i++) {
        int a, b;
        std::cin >> a >> b;
        ranges.push_back({a, b, i});
    }

    std::sort(ranges.begin(), ranges.end(), [](const Range& r1, const Range& r2) {
        return (r1.start < r2.start) || (r1.start == r2.start && r1.end > r2.end);
    });

    std::vector<int> contains(n, 0);
    std::vector<int> contained(n, 0);

    int maxend = std::numeric_limits<int>::min();
    int minend = std::numeric_limits<int>::max();

    for (int i = 0; i < n; i++) {
        if (ranges[i].end <= maxend) {
            contained[ranges[i].index] = 1;
        }
        maxend = std::max(maxend, ranges[i].end);
    }

    for (int i = n - 1; i >= 0; i--) {
        if (ranges[i].end >= minend) {
            contains[ranges[i].index] = 1;
        }
        minend = std::min(minend, ranges[i].end);
    }

    for (int i = 0; i < n; i++) {
        std::cout << contains[i] << " ";
    }
    std::cout << std::endl;

    for (int i = 0; i < n; i++) {
        std::cout << contained[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}