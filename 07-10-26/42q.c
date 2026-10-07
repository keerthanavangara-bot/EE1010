// Keerthana
// 7-10-26

#include <stdio.h>

// F = Σ(0, 2, 4, 8, 10, 11, 12)
int F(int b3, int b2, int b1, int b0) {
    int idx = (b3 << 3) | (b2 << 2) | (b1 << 1) | b0;
    return (idx == 0) || (idx == 2) || (idx == 4) || (idx == 8)
        || (idx == 10) || (idx == 11) || (idx == 12);
}

int main() {
    printf("b3 b2 b1 b0 | F\n");
    printf("----------------\n");

    for (int i = 0; i < 16; i++) {
        int b3 = (i >> 3) & 1;
        int b2 = (i >> 2) & 1;
        int b1 = (i >> 1) & 1;
        int b0 = (i >> 0) & 1;

        printf(" %d  %d  %d  %d | %d\n", b3, b2, b1, b0, F(b3, b2, b1, b0));
    }

    return 0;
}
