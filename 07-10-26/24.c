// Keerthana
// 7-10-26

#include <stdio.h>

// Extract bit i from num (0 = rightmost)
int getBit(int num, int i) {
    return (num >> i) & 1;
}

// X = 1 when at least two inputs are 1
int X(int a, int b, int c) {
    return (a & b) | (b & c) | (a & c);
}

int main() {
    int n = 3;
    int total = 1 << n;   // 2^n rows

    printf("a b c | X\n");
    printf("---------\n");

    for (int i = 0; i < total; i++) {
        int a = getBit(i, 2);
        int b = getBit(i, 1);
        int c = getBit(i, 0);

        printf("%d %d %d | %d\n", a, b, c, X(a, b, c));
    }

    return 0;
}
