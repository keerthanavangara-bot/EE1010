// Keerthana
// 7-10-26

#include <stdio.h>

// Print n bits of num (MSB first)
void printBits(int num, int n) {
    for (int i = n - 1; i >= 0; i--)
        printf("%d ", (num >> i) & 1);
}

// X = majority: 1 when at least two bits are 1
// Works for any n by counting set bits
int X(int num, int n) {
    int count = 0;
    for (int i = 0; i < n; i++)
        count += (num >> i) & 1;   // count the 1s
    return count >= 2;
}

int main() {
    int n = 3;              // change to any number
    int total = 1 << n;     // 2^n rows

    printf("bits | X\n");
    printf("-----\n");

    for (int i = 0; i < total; i++) {
        printBits(i, n);              // print all n bits
        printf("| %d\n", X(i, n));    // feed the whole number
    }

    return 0;
}
