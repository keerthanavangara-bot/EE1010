// Keerthana
// 7-10-26

#include <stdio.h>

// Original F = Σ(0, 2, 4, 8, 10, 11, 12)
// Using boolean logic: build index, check against each minterm
int F_original(int b3, int b2, int b1, int b0) {
    int idx = (b3 << 3) | (b2 << 2) | (b1 << 1) | b0;
    return (idx == 0) || (idx == 2) || (idx == 4) || (idx == 8)
        || (idx == 10) || (idx == 11) || (idx == 12);
}

// Option A: b1'b0' + b2'b0' + b1 b2' b3
int F_A(int b3, int b2, int b1, int b0) {
    return (!b1 && !b0) || (!b2 && !b0) || (b1 && !b2 && b3);
}

// Option B: b1'b0' + b2'b0'
int F_B(int b3, int b2, int b1, int b0) {
    return (!b1 && !b0) || (!b2 && !b0);
}

// Option C: b2'b0' + b1 b2 b3
int F_C(int b3, int b2, int b1, int b0) {
    return (!b2 && !b0) || (b1 && b2 && b3);
}

// Option D: b0'b2' + b3'
int F_D(int b3, int b2, int b1, int b0) {
    return (!b0 && !b2) || !b3;
}

int main() {
    int okA = 1, okB = 1, okC = 1, okD = 1;

    printf("b3 b2 b1 b0 | F | A | B | C | D\n");
    printf("--------------------------------\n");

    for (int i = 0; i < 16; i++) {
        int b3 = (i >> 3) & 1;
        int b2 = (i >> 2) & 1;
        int b1 = (i >> 1) & 1;
        int b0 = (i >> 0) & 1;

        int F = F_original(b3, b2, b1, b0);
        int A = F_A(b3, b2, b1, b0);
        int B = F_B(b3, b2, b1, b0);
        int C = F_C(b3, b2, b1, b0);
        int D = F_D(b3, b2, b1, b0);

        if (A != F) okA = 0;
        if (B != F) okB = 0;
        if (C != F) okC = 0;
        if (D != F) okD = 0;

        printf(" %d  %d  %d  %d | %d | %d | %d | %d | %d\n",
               b3, b2, b1, b0, F, A, B, C, D);
    }

    printf("\n--- Result ---\n");
    printf("A: %s\n", okA ? "CORRECT" : "WRONG");
    printf("B: %s\n", okB ? "CORRECT" : "WRONG");
    printf("C: %s\n", okC ? "CORRECT" : "WRONG");
    printf("D: %s\n", okD ? "CORRECT" : "WRONG");

    return 0;
}
