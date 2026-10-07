// Keerthana
// 7-10-26

#include <stdio.h>

// Fill array with binary bits of num (MSB first)
void int_to_binary_array(int num, int bits[], int size) {
    for (int i = 0; i < size; i++)
        bits[size - 1 - i] = (num >> i) & 1;
}

// X = 1 when at least two inputs are 1
int X(int a, int b, int c) {
    return (a && b) || (b && c) || (a && c);
}

int main() {
    int passA = 0, passB = 0, passC = 0, passD = 0;

    // 5 variables -> 32 rows
    for (int i = 0; i < 32; i++) {
        int bit[5];
        int_to_binary_array(i, bit, 5);

        int a = bit[0], b = bit[1], c = bit[2], d = bit[3], e = bit[4];

        // (A) X(a, b, X(c, d, e)) == X(X(a, b, c), d, e)
        passA += (X(a, b, X(c, d, e)) == X(X(a, b, c), d, e));

        // (B) X(a, b, X(a, b, c)) == X(a, b, c)
        passB += (X(a, b, X(a, b, c)) == X(a, b, c));

        // (C) X(a, b, X(a, c, d)) == (X(a, b, a) AND X(c, d, c))
        passC += (X(a, b, X(a, c, d)) == (X(a, b, a) && X(c, d, c)));

        // (D) X(a, b, c) == X(a, X(a, b, c), X(a, c, c))
        passD += (X(a, b, c) == X(a, X(a, b, c), X(a, c, c)));
    }

    // A column is CORRECT only if it holds for all 32 rows
    printf("A: %s\n", passA == 32 ? "CORRECT" : "WRONG");
    printf("B: %s\n", passB == 32 ? "CORRECT" : "WRONG");
    printf("C: %s\n", passC == 32 ? "CORRECT" : "WRONG");
    printf("D: %s\n", passD == 32 ? "CORRECT" : "WRONG");

    return 0;
}
